from mylib.bot import scrape
import click



@click.command()
@click.option('--name', 
              help='Web page we want to scrape.')


def cli(name):
    result=scrape(name)
    #print(result)
    click.echo(click.style(f" {result} ", bg="white", fg="blue"))

if __name__ == '__main__':
    cli()


