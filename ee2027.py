import numpy as np
import sympy


class Diode:
    def __init__(self, nVT, voltage_across_diode, voltage_source, resistor):
        """

        :param nVT:
        :param voltage_across_diode: Uses Volts
        :param voltage_source: Uses Volts
        :param resistor: Uses in ohms not kilo-ohms, mega-ohms etc.
        """
        self.nVT = nVT
        self.voltage_across_diode = voltage_across_diode
        self.voltage_source = voltage_source
        self.resistor = resistor

    def large_signal_model(self, d_VD, d_ID):
        """
        Determine the diode current and diode voltage by performing iterative approach because of the exponential
        IV characteristic of the pn-junction diode. We perform KVL equation of a simple diode circuit consisting of
        a DC voltage source, a resistor and a diode and use the diode equations repeatedly for a better estimate.

        Note: It is to be noted that d_VD and d_ID are the initial conditions, possible measured from the real circuit or
        obtained analytically using circuit analysis techniques.

        :param d_VD : This is the initial voltage, then a certain amount of current passes through the diode
        :param d_ID : This is the diode's current when there exists a certain amount of voltage across it.
        """

        for _ in range(10):
            # KVL equation to get the current through the diode
            current_through_diode = (self.voltage_source - self.voltage_across_diode) / self.resistor

            # Obtain new voltage_across_diode
            self.voltage_across_diode = (self.nVT * np.log(current_through_diode / d_ID)) + d_VD

        return self.voltage_across_diode, current_through_diode


class BJT:
    def __init__(self):
        pass


class MOSFET:
    def __init__(self):
        pass


class OPAMP:
    def __init__(self):
        pass


d = Diode(0.043, 0.7, 5, 1000)
print(d.large_signal_model(0.6, 0.001))
