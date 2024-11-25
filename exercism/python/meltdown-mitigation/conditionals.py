"""Functions to prevent a nuclear meltdown."""

from typing import Union


def is_criticality_balanced(
    temperature: Union[int, float], neutrons_emitted: Union[int, float]
) -> bool:
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(
    voltage: Union[int, float],
    current: Union[int, float],
    theoretical_max_power: Union[int, float],
) -> str:
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds
                                  to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    # Calculate the generated power as voltage * current
    generated_power = voltage * current

    # Calculate the efficiency percentage
    efficiency = (generated_power / theoretical_max_power) * 100

    # Classify efficiency into one of the four bands based on percentage
    if efficiency >= 80:  # 80% or more
        return "green"
    if efficiency >= 60:  # Between 60% and 80%
        return "orange"
    if efficiency >= 30:  # Between 30% and 60%
        return "red"
    return "black"


def fail_safe(
    temperature: Union[int, float],
    neutrons_produced_per_second: Union[int, float],
    threshold: Union[int, float],
) -> str:
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    # Calculate the reactor's current status as the product of temperature
    # and neutron flux
    reactor_status = temperature * neutrons_produced_per_second

    # Condition 1: Reactor status is less than 90% of the threshold
    if reactor_status < 0.9 * threshold:
        return "LOW"

    # Condition 2: Reactor status is within 10% of the threshold
    # (i.e., between 90% and 110% of the threshold)
    if 0.9 * threshold <= reactor_status <= 1.1 * threshold:
        return "NORMAL"

    # Condition 3: Reactor status exceeds 110% of the threshold
    return "DANGER"
