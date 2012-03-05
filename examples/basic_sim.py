from migen.fhdl.structure import *
from migen.sim.generic import Simulator
from migen.sim.icarus import Runner

class Counter:
	def __init__(self):
		self.count = Signal(BV(4))
	
	def do_simulation(self, s, cycle):
		print("Cycle: " + str(cycle) + " Count: " + str(s.rd(self.count)))
	
	def get_fragment(self):
		sync = [self.count.eq(self.count + 1)]
		sim = [self.do_simulation]
		return Fragment(sync=sync, sim=sim)

dut = Counter()
sim = Simulator(dut.get_fragment(), Runner())
sim.run(10)
