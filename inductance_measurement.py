import visa, statistics
resources = visa.ResourceManager()
resources.list_resources()
#lcrmeter = resources.open_resource('GPIB0::17::INSTR', write_termination = '\r',read_termination='\r')
lcrmeter = resources.open_resource('GPIB0::17::INSTR')
print(lcrmeter.query('*IDN?'))
lcrmeter.write(':BIAS:VOLT +0.00000E+00;STAT 0;')
lcrmeter.write(':CORR:LENG +2;METH SING;')
lcrmeter.write(':CORR:OPEN:STAT 0;')
lcrmeter.write(':CORR:SHOR:STAT 0;')
lcrmeter.write(':CORR:LOAD:STAT 0;TYPE LSRS;')
lcrmeter.write(':CORR:SPOT1:STAT 1;FREQ +1.00000E+06;LOAD:STAN +9.99999E-14,+6.28318E-10;')
lcrmeter.write(':CORR:SPOT2:STAT 0;FREQ +1.00000E+03;LOAD:STAN +1.59155E-04,+1.00000E+00;')
lcrmeter.write(':CORR:SPOT3:STAT 0;FREQ +1.00000E+03;LOAD:STAN +1.59155E-04,+1.00000E+00;')
lcrmeter.write(':CORR:USE +0;')
lcrmeter.write(':FUNC:IMP:TYPE LSRS;RANG +1.00000E+02;RANG:AUTO 0;')
lcrmeter.write(':FUNC:SMON:VAC:STAT 1;')
lcrmeter.write(':FUNC:SMON:IAC:STAT 1;')
#lcrmeter.write(':FUNC:DEV1:MODE OFF;REF +0.00000E+00;:FUNC:DEV2:MODE OFF;REF +0.00000E+00;:APER SHOR,+1;')
lcrmeter.write(':FUNC:DEV1:MODE OFF;REF +0.00000E+00;:FUNC:DEV2:MODE OFF;REF +0.00000E+00;:APER MED,+1;')
lcrmeter.write(':TRIG:SOUR BUS;DEL +0.00000E+00;')
lcrmeter.write(':DISP:PAGE MEAS;LINE \"PYTHON\";')
lcrmeter.write(':FORM ASC;')
lcrmeter.write(':COMP:STAT 0;MODE PTOL;TOL:NOM +0.00000E+00;')
lcrmeter.write(':COMP:ABIN 0;SWAP 0;BIN:COUN 0;')
lcrmeter.write(':LIST:MODE SEQ')
lcrmeter.write('*CLS')
lcrmeter.write('STAT:OPER:ENAB 16')
lcrmeter.write('*SRE 16')
lcrmeter.write('*ESE 255')
lcrmeter.write(':INIT:CONT ON;')

#lcrmeter.write(':BIAS:CURR 3 MA')
#lcrmeter.write('VOLT 25 MV')
lcrmeter.write(':CURR 3 MA')
lcrmeter.write(':APER MED')

inductance =[]
for i in range (5):
    lcrmeter.write('TRIG')
    [value1, value2, value3]= lcrmeter.query_ascii_values('FETC?')
    inductance.append(value1*1e9)
    print('Inductance: '+ str(inductance[i]))
    print('Resistance: '+ str(value2))

print("Inductance Mean is % s" % statistics.mean(inductance))
print("Inductance Standard Deviation is % s" % statistics.stdev(inductance))
print("Measurement Count is % s" % len(inductance))
