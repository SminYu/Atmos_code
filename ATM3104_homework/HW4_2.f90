program problem4_2
integer Ta, Tb, Tc
real Pwa, Pwb, Pwc, Psfc, Tsfc
real Ha, Hb, Hc, Pa, Pb, Pc, g, R, gamma

R=287.0
g=9.8
gamma=6.5/1000.0
Psfc=1013.25
Tsfc=293

Ha=1524
Hb=4267
Hc=8839

Pa=Psfc*((1-gamma*Ha/Tsfc)**(g/R/gamma))
Pb=Psfc*((1-gamma*Hb/Tsfc)**(g/R/gamma))
Pc=Psfc*((1-gamma*Hc/Tsfc)**(g/R/gamma))

do Ta=273,473
    Pwa=10**(-2937.4/Ta-4.9283*log10(real(Ta))+23.5471)
    If (abs(Pwa-Pa) .LE. 50) then
        print *, 'Denver', abs(Pwa-Pa), Ta
    else
    end if
end do

do Tb=273,473
    Pwb=10**(-2937.4/Tb-4.9283*log10(real(Tb))+23.5471)
    If (abs(Pwb-Pb) .LE. 50) then
        print *, 'NA divide', abs(Pwb-Pb), Tb
    else
    end if
end do

do Tc=273,473
    Pwc=10**(-2937.4/Tc-4.9283*log10(real(Tc))+23.5471)
    If (abs(Pwc-Pc) .LE. 50) then
        print *, 'Everst', abs(Pwc-Pc), Tc
    else
    end if
end do

stop
end