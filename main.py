import click
from coffee import *
import matplotlib.pyplot as plt

@click.command()
@click.option('--t', default=5, help='How many minutes we graph. One data point per minute')
@click.option('--m', default=120, help='The mass of milk used in grams')
@click.option('--e', default=200, help='The mass of expressso used in grams')
@click.option('--i', default=100, help='The mass of ice used in grams')
@click.option('--o', default='m',help='The order of which is added first, milk or ice. It is assumed that they are added at the very start, one after the other e.g m for milk first')
@click.option('--te', default=85, help='The temperature of the espresso shot')
@click.option('--tm', default=5, help='The temperature of the milk')


def generateTable(t, m, e, i, o, te, tm):
    click.echo(f"time: {t}, \nmass of milk: {m}, \nmass of espresso: {e}, \nmass of ice: {i}, \nWhich is added first milk or ice: {o},\nTemp of espresso shot: {te},\nTemp of milk: {tm}") # click.echo prints to the command line



    # The arrarys to hold the data
    time_steps = []
    list_of_temps = []
    list_of_milk_percentages = [] # the proportion of the liquid that is milk
    list_of_espresso_percentages = [] # the proportion of the liquid that is espresso
    list_of_water_percentages = [] # # the proportion of the liquid that is melted ice + espresso
    list_of_mass_of_unmelted_ice = []

    # We do this outside the loop because we want to show the temp before the milk and ice are added
    # current_temp = te
    # time_steps.append(0)
    # list_of_temps.append(current_temp)
    # list_of_milk_percentages.append(0)
    # list_of_espresso_percentages.append(100)
    # list_of_water_percentages.append(100)
    # list_of_mass_of_unmelted_ice.append(0)


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
        time_steps.append(time_step) # we've already appended the datapoint at t = 0
        list_of_temps.append(round(my_coffee.temp))
        list_of_milk_percentages.append(round(my_coffee.percentage_of_liquid_which_is_milk))
        list_of_espresso_percentages.append(round(my_coffee.percentage_of_liquid_which_is_espresso))
        list_of_water_percentages.append(round(my_coffee.percentage_of_liquid_which_is_water))
        list_of_mass_of_unmelted_ice.append(round(my_coffee.mass_ice))


    # Print the info to the console 
    click.echo(time_steps)
    click.echo(list_of_temps)
    click.echo(list_of_milk_percentages)
    click.echo(list_of_espresso_percentages)


    # Plot the data
    plt.subplot(2, 2, 1)  # 1 row, 2 columns, index 1
    plt.plot(time_steps, list_of_temps,label='Temperature', color='red')
    plt.xlabel('Time (mins)')
    plt.ylabel('Coffee Temperature (°C)')
    plt.title('Coffee Temperature over Time')
    plt.legend()

    plt.subplot(2, 2, 2)  # 1 row, 2 columns, index 2
    plt.plot(time_steps, list_of_espresso_percentages,label='Espresso', color='brown')
    plt.plot(time_steps, list_of_milk_percentages,label='Milk', color='black')
    plt.plot(time_steps, list_of_water_percentages,label='Espresso + Melted ice', color='green')
    plt.xlabel('Time (mins)')
    plt.ylabel('% of overall coffee')
    plt.title('Compostition of the coffee over time')
    plt.legend()

    plt.subplot(2, 2, 3)  # 1 row, 2 columns, index 1
    plt.plot(time_steps, list_of_mass_of_unmelted_ice,label='Unmelted ice', color='blue')
    plt.xlabel('Time (mins)')
    plt.ylabel('Mass of ice (g)')
    plt.title('Mass of ice over time')
    plt.legend()

    plt.subplots_adjust(hspace=0.5)
    plt.show()


if __name__ == '__main__':
    generateTable()

