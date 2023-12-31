import textwrap

import click
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning # pylint: disable=import-error

from . import __version__

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # pylint: disable=no-member
    with requests.get(API_URL, timeout=30, verify=False) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
    