import click

@click.command()
@click.option('--t', default=20, help='How many minutes we graph. One data point per minute')
@click.option('--m', default=100, help='The mass of milk used in grams')
@click.option('--e', default=100, help='The mass of expressso used in grams')
@click.option('--i', default=0, help='The mass of ice used in grams')
@click.option('--o', default='m',help='The order of which is added first, milk or ice. It is assumed that they are added at the very start, one after the other e.g m for milk first')
@click.option('--te', default=85, help='The temperature of the espresso shot')
@click.option('--tm', default=5, help='The temperature of the milk')


def generateTable(t, m, e, i, o, te, tm):
    click.echo(f"time: {t}, \nmass of milk: {m}, \nmass of espresso: {e}, \nmass of ice: {i}, \nWhich is added first milk or ice: {o},\nTemp of espresso shot: {te},\nTemp of milk: {tm}") # click.echo prints to the command line

    # Returns the temperature after adding the milk. We assume instant temperature shift 
    def add_milk(mass_espresso, temp_espresso, mass_milk, temp_milk):
        return ((mass_espresso * temp_espresso) + (mass_milk * temp_milk)) / (mass_espresso + mass_milk)
    

    def add_ice(mass_coffee, current_temp, mass_ice, time_step, melt_rate):
        


        return new_temp
    
    def melt_ice(mass_coffee, current_temp, mass_ice):
        # Calculates the total energy in the system at the start
        energy_total = mass_coffee * specific_heat * current_temp

        melt_rate = 5  # in grams per minute per degree Celsius
        specific_heat = 4.186  # Specific heat capacity of water (joules per gram degree celsius)
        latent_heat_fusion = 334  # latent heat of fusion for ice (joules per gram)

        # Simulates the melting of the ice over time
        if mass_ice > 0:
            # Calculates how much ice melts in this time step
            melt = min(mass_ice, melt_rate * current_temp * time_step)
            
            # Calculates the energy needed to melt the ice and subtracts it from the total
            energy_total -= melt * latent_heat_fusion

            # Update the masses
            mass_coffee += melt
            mass_ice -= melt

            # Calculate the new temperature of the coffee
            new_temp = energy_total / (mass_coffee * specific_heat)
        else:
            new_temp = current_temp # if there is no ice left to melt, we keep the mass of coffee, mass of ice and temp of coffee the same

        return mass_coffee, mass_ice, new_temp




    # The arrarys to hold the data
    time_steps = []
    list_of_temps = []

    # We do this outside the loop because we want to show the temp before the milk and ice are added
    current_temp = te
    time_steps.append(0)
    list_of_temps.append(current_temp)

    # We are checking the order in which we are adding the milk and ice
    if o == 'm':
        current_temp = add_milk(e, te, m, tm)

    # Loop through all the timesteps and calculate the data at each point
    for time_step in range(t):
        time_steps.append(time_step + 1) # we've already appended the datapoint at t = 0
        list_of_temps.append(current_temp)

    # Print the info to the console 
    click.echo(time_steps)
    click.echo(list_of_temps)


if __name__ == '__main__':
    generateTable()


