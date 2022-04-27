"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800 and neutrons_emitted>500 and temperature*neutrons_emitted<500000):
       return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    eff= (generated_power/theoretical_max_power)*100
    if(eff>=80):
        return 'green'
    elif(eff>=60):
        return 'orange'
    elif(eff>=30):
        return 'red'
    else:
        return 'black'
        
      


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if ((temperature * neutrons_produced_per_second) < threshold*0.9):
        return 'LOW'
    elif ((temperature * neutrons_produced_per_second)<= threshold*1.1):
        return 'NORMAL'
    else:
        return 'DANGER'
