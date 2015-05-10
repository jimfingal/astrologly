import markdown
import os

def get_homepage():
    script_dir = os.path.dirname(__file__) 
    rel_path = "../../Readme.md"
    file_path = os.path.join(script_dir, rel_path)

    with open(file_path) as f:
        content = f.read()
        return markdown.markdown(
            content,
            extensions=['extra',
                        'codehilite',
                        'toc',
                        'wikilinks']
        )
