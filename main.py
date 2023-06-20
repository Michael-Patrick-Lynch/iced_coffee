import click
from coffee import *

@click.command()
@click.option('--t', default=20, help='How many minutes we graph. One data point per minute')
@click.option('--m', default=100, help='The mass of milk used in grams')
@click.option('--e', default=100, help='The mass of expressso used in grams')
@click.option('--i', default=40, help='The mass of ice used in grams')
@click.option('--o', default='m',help='The order of which is added first, milk or ice. It is assumed that they are added at the very start, one after the other e.g m for milk first')
@click.option('--te', default=85, help='The temperature of the espresso shot')
@click.option('--tm', default=5, help='The temperature of the milk')


def generateTable(t, m, e, i, o, te, tm):
    click.echo(f"time: {t}, \nmass of milk: {m}, \nmass of espresso: {e}, \nmass of ice: {i}, \nWhich is added first milk or ice: {o},\nTemp of espresso shot: {te},\nTemp of milk: {tm}") # click.echo prints to the command line



    # The arrarys to hold the data
    time_steps = []
    list_of_temps = []

    # We do this outside the loop because we want to show the temp before the milk and ice are added
    current_temp = te
    time_steps.append(0)
    list_of_temps.append(current_temp)

    # Initalise the coffee object
    my_coffee = coffee(temp_espresso= te,mass_espresso= e)

    # We are checking the order in which we are adding the milk and ice
    if o == 'm':
        my_coffee.add_milk(mass_of_milk_to_add=m, temp_milk=tm)
        my_coffee.add_ice(mass_of_ice_to_add= i)
    elif o == 'i':
        my_coffee.add_ice(mass_of_ice_to_add= i)
        my_coffee.add_milk(mass_of_milk_to_add=m, temp_milk=tm)

    # Loop through all the timesteps and calculate the data at each point
    for time_step in range(t):
        my_coffee.melt_ice()
        time_steps.append(time_step + 1) # we've already appended the datapoint at t = 0
        list_of_temps.append(round(my_coffee.temp))

    # Print the info to the console 
    click.echo(time_steps)
    click.echo(list_of_temps)


if __name__ == '__main__':
    generateTable()

