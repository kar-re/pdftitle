from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
import click
import os
import sys
from pathlib import Path

@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Will print verbose messages.", default=False)  
@click.argument('input')
@click.argument('output')
def cli(verbose, input, output):
    """
        input: input file or files

        output: output folder, will create if not found. 
    """
    if verbose:
        click.echo(f"Current args: {input} {output}")
    
    path = Path(input)
    folder = path.resolve()
    file_name = '.'
    
    if path.is_file():
        folder = path.absolute().parent
        file_name = path.name
    if verbose:
        click.echo(f"Current path: {path} {folder} {path.name}")
    
    files = [entry.path for entry in os.scandir(folder) if file_name in entry.name and entry.name.endswith('.pdf')]
    
    if verbose:
        click.echo(f"Found {len(files)} files")
    number = 1
    out_path = os.path.realpath(output)

    if not os.path.exists(out_path):
        try:
            os.makedirs(out_path)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    for file in files:
        out_file = os.path.join(out_path, file)
        trailer = PdfReader(file)

        if trailer.Info and trailer.Info.Title:
            click.echo(f'Current title: {trailer.Info.Title}')
        else:
            click.echo("Current file doesn't have an existing title")
            if not trailer.Info:
                trailer.Info = IndirectPdfDict(
                    Title='your title goes here',
                    Author='Title change',
                    Subject='This is a file with a changed title',
                    Creator='Title Change 0.1',
                )

        trailer.Info.Title = click.prompt(f'Write the new metadata title for {file}', type=str)

        PdfWriter(out_file, trailer=trailer).write()

        if verbose:
            click.echo(f"Wrote {os.path.basename(file)}, {number}/{len(files)}")
        
        number += 1

    click.echo('Done!')



