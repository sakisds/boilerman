""" 
Boilerman v0.1.0
http://github.com/sakisds/boilerman
"""

import argparse
import os
import sys
import yaml
import pystache
import signal
from .util import *

def handle_arguments():
    """
    Handle the command line arguments.
    """
    parser = argparse.ArgumentParser("boilerman", description="A general purpose boilerplate generator")
    parser.add_argument('template', help='Template to generate', type=str)
    args = parser.parse_args()
    
    if args.template[-5:] != '.yaml':
        args.template += '.yaml'
        
    return args

def main(args=None):
    # Handle CTRL+C
    signal.signal(signal.SIGINT, lambda x,y: sys.exit(signal.SIGINT))
    
    # Grab command line arguments
    args = handle_arguments()

    # Load template from disk
    definitionPath = os.path.join(os.environ.get('BOILERMAN_TEMPLATES', os.path.expanduser('~/.boilerman')), args.template)
    definition = load_file_as_str(definitionPath)
        
    # Parse each YAML document
    try:
        documents = yaml.safe_load_all(definition)
    except yaml.YAMLError as ex:
        sys.exit("Error in template file: %s" % ex)

    # Create every document
    for doc in documents:
        # Print file name & description
        print("%s - %s" % (doc['filepath'], doc['title']))
        # Ask user what to fill in for each variable
        if 'variables' in doc: 
            parsedVariables = {}
            for variable in doc['variables']:
                parsedVariables[variable["name"]] = prompt("%s (%s): " % (variable["name"], variable["description"]))
                
        # Load template
        templatePath = os.path.join(os.environ.get('BOILERMAN_TEMPLATES', os.path.expanduser('~/.boilerman')), doc['filepath'])
        template = load_file_as_str(templatePath)
        # Add delimiter tag to template
        if 'delimiters' in doc:
            template = '{{=%s=}}\n%s' % (doc['delimiters'], template)
        
        # Render template
        output = pystache.render(template, parsedVariables)
        with open(doc['filepath'], 'w') as outputFile:
            outputFile.write(output);
               
        # Print a newline
        print()
        
if __name__ == "__main__":
    main()