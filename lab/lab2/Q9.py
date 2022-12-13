def virus_growth(start_infected, growth_rate, growth_period, growth_time):
    return start_infected * (growth_rate**(growth_time/growth_period))