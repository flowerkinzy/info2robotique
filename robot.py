import nxt, thread, time
b = nxt.find_one_brick()
mA = nxt.Motor(b, nxt.PORT_B)
mB =nxt.Motor(b, nxt.PORT_C)
lux = nxt.sensor.Color20(b,nxt.PORT_3)
#mA.run(100) ; mB.run(100) ; time.sleep(1); mA.brake(); mB.brake()
#mA.weak_turn(100,90)



def main():
    while 1:
        intensite =lux.get_reflected_light(nxt.sensor.Type.COLORNONE)
        if intensite<80:
            print str(intensite)+" noir"
            mA.run(90); mB.run(80); time.sleep(0.8); mA.brake(); mB.brake()
            angle=15
        else:
            print str(intensite)+" blanc"
            if angle<45:
                angle=angle+7
            else:
                angle=15
                
            mA.turn(100,angle)
            mA.run(85); mB.run(75); time.sleep(0.1); mA.brake(); mB.brake()
            if intensite<80:
                print str(intensite)+" noir"
                mA.run(90); mB.run(80); time.sleep(0.8); mA.brake(); mB.brake()
                angle=15
            else:
                print str(intensite)+" blanc"
                mA.turn(-100,2*angle)
                mA.run(85); mB.run(75); time.sleep(0.1); mA.brake(); mB.brake()


def terminer():
    mA.run(0)
    mB.run(0)
    exit(0)
    

try:
    main()
    terminer()
except KeyboardInterrupt:
    terminer()