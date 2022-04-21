import visa, statistics
resources = visa.ResourceManager()
resources.list_resources()
#lcrmeter = resources.open_resource('GPIB0::17::INSTR', write_termination = '\r',read_termination='\r')
lcrmeter = resources.open_resource('GPIB0::17::INSTR')
print(lcrmeter.query('*IDN?'))
cap =[]
for i in range (5):
    lcrmeter.write('TRIG')
    [value1, value2, value3]= lcrmeter.query_ascii_values('FETC?')
    cap.append(value1*1e12)
    print(cap[i])

print("Capacitance Mean is % s" % statistics.mean(cap))
print("Capacitance Standard Deviation is % s" % statistics.stdev(cap))
