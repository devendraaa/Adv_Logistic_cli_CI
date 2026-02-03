from mylib.logistic import (
    distance_between_two_points,
    get_coordinates,
    travel_time,
    cities_list,
)
import click


@click.group()
def cli():
    """tool for calculating total distance between a list of the cities"""


@cli.command("cities")
def cities():
    """list of all cities"""

    click.echo(click.style("list of cities", fg="green"))
    for city in cities_list():
        click.echo(click.style(city, fg="blue"))


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """
    Distance between two cities

    :param city1: Description
    :param city2: Description
    """

    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(
        click.style(
            f"{distance_between_two_points(get_coordinates(city1), get_coordinates(city2))} miles",
            fg="blue",
        )
    )


if __name__ == "__main__":
    cli()
