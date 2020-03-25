#!/usr/bin/env python3
import sys
from cpu import *

cpu = CPU()

cpu.load('\examples\mult.ls8')
cpu.run()