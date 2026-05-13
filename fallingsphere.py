steps = 10000 #of sim per second
sphereDiam = 1 #metres
sphereDens = 60 #kg/m^3
distToFall = 5 #metres

sphereA = ((sphereDiam/2)**2)*3.14159265359
sphereV = ((sphereDiam/2)**3)*3.14159265359*4/3
sphereM = sphereV*sphereDens

gravity = 9.8183 #m/s^2
airDen = 1.204 #kg/m^3
airViscos = 0.00001849 #kg/(m*s)

distance = 0 #m fallen
velocity = 0 #m/s
curStep = 0
airRes : float #m/s^2
bouyForce : float #m/s^2
ReyN : float #dimensionless
dragC : float #dimensionless
while -distToFall<distance<distToFall:
    curStep+=1
    
    if velocity!=0:
        ReyN = (airDen*sphereDiam*abs(velocity))/airViscos
        dragC = 24/ReyN+(2.6*ReyN/5)/(1+(ReyN/5)**1.52)+(0.411*(ReyN/263000)**(-7.94))/(1+(ReyN/263000)**(-8))+(0.25*ReyN/1000000)/(1+ReyN/1000000)
        airRes =(((velocity**2)*airDen*dragC*sphereA)/(sphereM*2))*velocity/abs(velocity)
        velocity-=airRes/steps
    
    bouyForce = (airDen*sphereV*gravity)/sphereM
    velocity-=bouyForce/steps

    velocity+=gravity/steps

    distance+=velocity/steps

print(f"{distance} meters in {curStep/steps} seconds")