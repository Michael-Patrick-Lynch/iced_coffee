# I will use an object to store the tempertature, mass of ice, mass of milk, mass of water and mass of espresso in the cup of coffee at any given time
class coffee:
    def  __init__(self, temp_espresso, mass_espresso):
       self.temp = temp_espresso # since every coffee starts as just an espresso shot, the mass and temp of the shot are the only arguments needed to initalise the object
       self.mass_ice = 0
       self.mass_milk = 0
       self.mass_water = 0
       self.mass_espresso = mass_espresso


   
    @property
    def proportion_of_liquid_which_is_milk(self):
        return self.mass_milk / (self.mass_milk + self.mass_water + self.mass_espresso)
   
    @property
    def mass_liquid(self): # the mass of liquid in the cup
        return self.mass_milk + self.mass_water + self.mass_espresso
   
    # Adding milk instantly changes the temperature, and increases the mass of milk in the coffee 
    def add_milk(self, mass_of_milk_to_add, temp_milk):
        self.temp = ((self.mass_liquid * self.temp) + (mass_of_milk_to_add * temp_milk)) / (self.mass_liquid + mass_of_milk_to_add)
        self.mass_milk += mass_of_milk_to_add
    

    def add_ice(self, mass_of_ice_to_add):
        self.mass_ice += mass_of_ice_to_add

    def melt_ice(self):
        melt_rate = 0.05  # in grams per minute per degree Celsius
        specific_heat = 4.186  # Specific heat capacity of water (joules per gram degree celsius)
        latent_heat_fusion = 334  # latent heat of fusion for ice (joules per gram)

        # Calculates the total energy in the system at the start (we neglect the energy due to the ice)
        energy_total = self.mass_liquid * specific_heat * self.temp


        # Simulates the melting of the ice over time
        if self.mass_ice > 0:
            # Calculates how much ice melts in this time step
            melt = min(self.mass_ice, melt_rate * self.temp)
            print(melt)
            
            # Calculates the energy needed to melt the ice and subtracts it from the total
            energy_total -= melt * latent_heat_fusion

            # Update the masses
            self.mass_water += melt
            self.mass_ice -= melt

            # Calculate the new temperature of the coffee
            self.temp = energy_total / (self.mass_liquid * specific_heat)

    
