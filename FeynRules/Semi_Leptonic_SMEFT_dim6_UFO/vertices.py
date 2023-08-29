# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.1 for Mac OS X x86 (64-bit) (June 19, 2020)
# Date: Tue 8 Mar 2022 14:57:43


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1467})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_1633})

V_3 = Vertex(name = 'V_3',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_1465})

V_4 = Vertex(name = 'V_4',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_1465})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_1466,(0,0):C.GC_1466,(2,2):C.GC_1466})

V_6 = Vertex(name = 'V_6',
             particles = [ P.b__tilde__, P.b, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1996})

V_7 = Vertex(name = 'V_7',
             particles = [ P.d__tilde__, P.d, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1998})

V_8 = Vertex(name = 'V_8',
             particles = [ P.s__tilde__, P.s, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2001})

V_9 = Vertex(name = 'V_9',
             particles = [ P.e__plus__, P.e__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1999})

V_10 = Vertex(name = 'V_10',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2000})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2003})

V_12 = Vertex(name = 'V_12',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_1997})

V_13 = Vertex(name = 'V_13',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2002})

V_14 = Vertex(name = 'V_14',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2004})

V_15 = Vertex(name = 'V_15',
              particles = [ P.c__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_141,(0,8):C.GC_141,(0,6):C.GC_2461,(0,9):C.GC_142,(0,0):C.GC_113,(0,3):C.GC_2344,(0,4):C.GC_2344,(0,11):C.GC_1337,(0,1):C.GC_2488,(0,2):C.GC_1085,(0,5):C.GC_2345,(0,10):C.GC_2316})

V_16 = Vertex(name = 'V_16',
              particles = [ P.c__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2470})

V_17 = Vertex(name = 'V_17',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2497,(0,9):C.GC_253,(0,7):C.GC_252,(0,8):C.GC_252,(0,0):C.GC_224,(0,11):C.GC_1338,(0,1):C.GC_2524,(0,2):C.GC_1086,(0,5):C.GC_2347,(0,3):C.GC_2346,(0,4):C.GC_2346,(0,10):C.GC_2317})

V_18 = Vertex(name = 'V_18',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2506})

V_19 = Vertex(name = 'V_19',
              particles = [ P.u__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2425,(0,9):C.GC_31,(0,7):C.GC_30,(0,8):C.GC_30,(0,0):C.GC_2,(0,11):C.GC_1336,(0,1):C.GC_2452,(0,2):C.GC_1084,(0,5):C.GC_2343,(0,3):C.GC_2342,(0,4):C.GC_2342,(0,10):C.GC_2315})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2434})

V_21 = Vertex(name = 'V_21',
              particles = [ P.c__tilde__, P.c, P.mu__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2462,(0,9):C.GC_160,(0,7):C.GC_159,(0,8):C.GC_159,(0,0):C.GC_122,(0,11):C.GC_1346,(0,1):C.GC_2489,(0,2):C.GC_1094,(0,5):C.GC_2351,(0,3):C.GC_2350,(0,4):C.GC_2350,(0,10):C.GC_2319})

V_22 = Vertex(name = 'V_22',
              particles = [ P.c__tilde__, P.c, P.mu__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2472})

V_23 = Vertex(name = 'V_23',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2498,(0,9):C.GC_271,(0,7):C.GC_270,(0,8):C.GC_270,(0,0):C.GC_233,(0,11):C.GC_1347,(0,1):C.GC_2525,(0,2):C.GC_1095,(0,5):C.GC_2353,(0,3):C.GC_2352,(0,4):C.GC_2352,(0,10):C.GC_2320})

V_24 = Vertex(name = 'V_24',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2508})

V_25 = Vertex(name = 'V_25',
              particles = [ P.u__tilde__, P.c, P.mu__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2426,(0,9):C.GC_49,(0,7):C.GC_48,(0,8):C.GC_48,(0,0):C.GC_11,(0,11):C.GC_1345,(0,1):C.GC_2453,(0,2):C.GC_1093,(0,5):C.GC_2349,(0,3):C.GC_2348,(0,4):C.GC_2348,(0,10):C.GC_2318})

V_26 = Vertex(name = 'V_26',
              particles = [ P.u__tilde__, P.c, P.mu__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2436})

V_27 = Vertex(name = 'V_27',
              particles = [ P.c__tilde__, P.c, P.ta__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2463,(0,9):C.GC_178,(0,7):C.GC_177,(0,8):C.GC_177,(0,0):C.GC_131,(0,11):C.GC_1355,(0,1):C.GC_2490,(0,2):C.GC_1103,(0,5):C.GC_2357,(0,3):C.GC_2356,(0,4):C.GC_2356,(0,10):C.GC_2322})

V_28 = Vertex(name = 'V_28',
              particles = [ P.c__tilde__, P.c, P.ta__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2474})

V_29 = Vertex(name = 'V_29',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,8):C.GC_288,(0,9):C.GC_288,(0,7):C.GC_2499,(0,10):C.GC_289,(0,0):C.GC_242,(0,3):C.GC_2358,(0,5):C.GC_2358,(0,12):C.GC_1356,(0,1):C.GC_2526,(0,2):C.GC_1104,(0,6):C.GC_2010,(0,4):C.GC_2313,(0,11):C.GC_2323})

V_30 = Vertex(name = 'V_30',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2510})

V_31 = Vertex(name = 'V_31',
              particles = [ P.u__tilde__, P.c, P.ta__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2427,(0,9):C.GC_67,(0,7):C.GC_66,(0,8):C.GC_66,(0,0):C.GC_20,(0,11):C.GC_1354,(0,1):C.GC_2454,(0,2):C.GC_1102,(0,5):C.GC_2355,(0,3):C.GC_2354,(0,4):C.GC_2354,(0,10):C.GC_2321})

V_32 = Vertex(name = 'V_32',
              particles = [ P.u__tilde__, P.c, P.ta__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2438})

V_33 = Vertex(name = 'V_33',
              particles = [ P.c__tilde__, P.c, P.e__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2464,(0,9):C.GC_148,(0,7):C.GC_147,(0,8):C.GC_147,(0,0):C.GC_116,(0,11):C.GC_1364,(0,1):C.GC_2491,(0,2):C.GC_1112,(0,5):C.GC_2362,(0,3):C.GC_2361,(0,4):C.GC_2361,(0,10):C.GC_2325})

V_34 = Vertex(name = 'V_34',
              particles = [ P.c__tilde__, P.c, P.e__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2476})

V_35 = Vertex(name = 'V_35',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2500,(0,9):C.GC_259,(0,7):C.GC_258,(0,8):C.GC_258,(0,0):C.GC_227,(0,11):C.GC_1365,(0,1):C.GC_2527,(0,2):C.GC_1113,(0,5):C.GC_2364,(0,3):C.GC_2363,(0,4):C.GC_2363,(0,10):C.GC_2326})

V_36 = Vertex(name = 'V_36',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2512})

V_37 = Vertex(name = 'V_37',
              particles = [ P.u__tilde__, P.c, P.e__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2428,(0,9):C.GC_37,(0,7):C.GC_36,(0,8):C.GC_36,(0,0):C.GC_5,(0,11):C.GC_1363,(0,1):C.GC_2455,(0,2):C.GC_1111,(0,5):C.GC_2360,(0,3):C.GC_2359,(0,4):C.GC_2359,(0,10):C.GC_2324})

V_38 = Vertex(name = 'V_38',
              particles = [ P.u__tilde__, P.c, P.e__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2440})

V_39 = Vertex(name = 'V_39',
              particles = [ P.c__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2465,(0,9):C.GC_166,(0,7):C.GC_165,(0,8):C.GC_165,(0,0):C.GC_125,(0,11):C.GC_1373,(0,1):C.GC_2492,(0,2):C.GC_1121,(0,5):C.GC_2368,(0,3):C.GC_2367,(0,4):C.GC_2367,(0,10):C.GC_2328})

V_40 = Vertex(name = 'V_40',
              particles = [ P.c__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2478})

V_41 = Vertex(name = 'V_41',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2501,(0,9):C.GC_277,(0,7):C.GC_276,(0,8):C.GC_276,(0,0):C.GC_236,(0,11):C.GC_1374,(0,1):C.GC_2528,(0,2):C.GC_1122,(0,5):C.GC_2370,(0,3):C.GC_2369,(0,4):C.GC_2369,(0,10):C.GC_2329})

V_42 = Vertex(name = 'V_42',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2514})

V_43 = Vertex(name = 'V_43',
              particles = [ P.u__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2429,(0,9):C.GC_55,(0,7):C.GC_54,(0,8):C.GC_54,(0,0):C.GC_14,(0,11):C.GC_1372,(0,1):C.GC_2456,(0,2):C.GC_1120,(0,5):C.GC_2366,(0,3):C.GC_2365,(0,4):C.GC_2365,(0,10):C.GC_2327})

V_44 = Vertex(name = 'V_44',
              particles = [ P.u__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2442})

V_45 = Vertex(name = 'V_45',
              particles = [ P.c__tilde__, P.c, P.ta__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2466,(0,9):C.GC_184,(0,7):C.GC_183,(0,8):C.GC_183,(0,0):C.GC_134,(0,11):C.GC_1382,(0,1):C.GC_2493,(0,2):C.GC_1130,(0,5):C.GC_2374,(0,3):C.GC_2373,(0,4):C.GC_2373,(0,10):C.GC_2331})

V_46 = Vertex(name = 'V_46',
              particles = [ P.c__tilde__, P.c, P.ta__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2480})

V_47 = Vertex(name = 'V_47',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2502,(0,9):C.GC_295,(0,7):C.GC_294,(0,8):C.GC_294,(0,0):C.GC_245,(0,11):C.GC_1383,(0,1):C.GC_2529,(0,2):C.GC_1131,(0,5):C.GC_2376,(0,3):C.GC_2375,(0,4):C.GC_2375,(0,10):C.GC_2332})

V_48 = Vertex(name = 'V_48',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2516})

V_49 = Vertex(name = 'V_49',
              particles = [ P.u__tilde__, P.c, P.ta__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2430,(0,9):C.GC_73,(0,7):C.GC_72,(0,8):C.GC_72,(0,0):C.GC_23,(0,11):C.GC_1381,(0,1):C.GC_2457,(0,2):C.GC_1129,(0,5):C.GC_2372,(0,3):C.GC_2371,(0,4):C.GC_2371,(0,10):C.GC_2330})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.c, P.ta__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2444})

V_51 = Vertex(name = 'V_51',
              particles = [ P.c__tilde__, P.c, P.e__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2467,(0,9):C.GC_154,(0,7):C.GC_153,(0,8):C.GC_153,(0,0):C.GC_119,(0,11):C.GC_1391,(0,1):C.GC_2494,(0,2):C.GC_1139,(0,5):C.GC_2380,(0,3):C.GC_2379,(0,4):C.GC_2379,(0,10):C.GC_2334})

V_52 = Vertex(name = 'V_52',
              particles = [ P.c__tilde__, P.c, P.e__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2482})

V_53 = Vertex(name = 'V_53',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2503,(0,9):C.GC_265,(0,7):C.GC_264,(0,8):C.GC_264,(0,0):C.GC_230,(0,11):C.GC_1392,(0,1):C.GC_2530,(0,2):C.GC_1140,(0,5):C.GC_2382,(0,3):C.GC_2381,(0,4):C.GC_2381,(0,10):C.GC_2335})

V_54 = Vertex(name = 'V_54',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2518})

V_55 = Vertex(name = 'V_55',
              particles = [ P.u__tilde__, P.c, P.e__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2431,(0,9):C.GC_43,(0,7):C.GC_42,(0,8):C.GC_42,(0,0):C.GC_8,(0,11):C.GC_1390,(0,1):C.GC_2458,(0,2):C.GC_1138,(0,5):C.GC_2378,(0,3):C.GC_2377,(0,4):C.GC_2377,(0,10):C.GC_2333})

V_56 = Vertex(name = 'V_56',
              particles = [ P.u__tilde__, P.c, P.e__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2446})

V_57 = Vertex(name = 'V_57',
              particles = [ P.c__tilde__, P.c, P.mu__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2468,(0,9):C.GC_172,(0,7):C.GC_171,(0,8):C.GC_171,(0,0):C.GC_128,(0,11):C.GC_1400,(0,1):C.GC_2495,(0,2):C.GC_1148,(0,5):C.GC_2386,(0,3):C.GC_2385,(0,4):C.GC_2385,(0,10):C.GC_2337})

V_58 = Vertex(name = 'V_58',
              particles = [ P.c__tilde__, P.c, P.mu__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2484})

V_59 = Vertex(name = 'V_59',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2504,(0,9):C.GC_283,(0,7):C.GC_282,(0,8):C.GC_282,(0,0):C.GC_239,(0,11):C.GC_1401,(0,1):C.GC_2531,(0,2):C.GC_1149,(0,5):C.GC_2388,(0,3):C.GC_2387,(0,4):C.GC_2387,(0,10):C.GC_2338})

V_60 = Vertex(name = 'V_60',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2520})

V_61 = Vertex(name = 'V_61',
              particles = [ P.u__tilde__, P.c, P.mu__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2432,(0,9):C.GC_61,(0,7):C.GC_60,(0,8):C.GC_60,(0,0):C.GC_17,(0,11):C.GC_1399,(0,1):C.GC_2459,(0,2):C.GC_1147,(0,5):C.GC_2384,(0,3):C.GC_2383,(0,4):C.GC_2383,(0,10):C.GC_2336})

V_62 = Vertex(name = 'V_62',
              particles = [ P.u__tilde__, P.c, P.mu__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2448})

V_63 = Vertex(name = 'V_63',
              particles = [ P.c__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2469,(0,9):C.GC_190,(0,7):C.GC_189,(0,8):C.GC_189,(0,0):C.GC_137,(0,11):C.GC_1409,(0,1):C.GC_2496,(0,2):C.GC_1157,(0,5):C.GC_2392,(0,3):C.GC_2391,(0,4):C.GC_2391,(0,10):C.GC_2340})

V_64 = Vertex(name = 'V_64',
              particles = [ P.c__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2486})

V_65 = Vertex(name = 'V_65',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2505,(0,9):C.GC_301,(0,7):C.GC_300,(0,8):C.GC_300,(0,0):C.GC_248,(0,11):C.GC_1410,(0,1):C.GC_2532,(0,2):C.GC_1158,(0,5):C.GC_2394,(0,3):C.GC_2393,(0,4):C.GC_2393,(0,10):C.GC_2341})

V_66 = Vertex(name = 'V_66',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2522})

V_67 = Vertex(name = 'V_67',
              particles = [ P.u__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2433,(0,9):C.GC_79,(0,7):C.GC_78,(0,8):C.GC_78,(0,0):C.GC_26,(0,11):C.GC_1408,(0,1):C.GC_2460,(0,2):C.GC_1156,(0,5):C.GC_2390,(0,3):C.GC_2389,(0,4):C.GC_2389,(0,10):C.GC_2339})

V_68 = Vertex(name = 'V_68',
              particles = [ P.u__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2450})

V_69 = Vertex(name = 'V_69',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2762,(0,9):C.GC_144,(0,7):C.GC_143,(0,8):C.GC_143,(0,0):C.GC_114,(0,11):C.GC_2789,(0,1):C.GC_1340,(0,2):C.GC_1088,(0,5):C.GC_2645,(0,3):C.GC_2644,(0,4):C.GC_2644,(0,10):C.GC_2616})

V_70 = Vertex(name = 'V_70',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2771})

V_71 = Vertex(name = 'V_71',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2763,(0,9):C.GC_162,(0,7):C.GC_161,(0,8):C.GC_161,(0,0):C.GC_123,(0,11):C.GC_2790,(0,1):C.GC_1349,(0,2):C.GC_1097,(0,5):C.GC_2651,(0,3):C.GC_2650,(0,4):C.GC_2650,(0,10):C.GC_2619})

V_72 = Vertex(name = 'V_72',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2773})

V_73 = Vertex(name = 'V_73',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2764,(0,9):C.GC_180,(0,7):C.GC_179,(0,8):C.GC_179,(0,0):C.GC_132,(0,11):C.GC_2791,(0,1):C.GC_1358,(0,2):C.GC_1106,(0,5):C.GC_2657,(0,3):C.GC_2656,(0,4):C.GC_2656,(0,10):C.GC_2622})

V_74 = Vertex(name = 'V_74',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2775})

V_75 = Vertex(name = 'V_75',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2765,(0,9):C.GC_150,(0,7):C.GC_149,(0,8):C.GC_149,(0,0):C.GC_117,(0,11):C.GC_2792,(0,1):C.GC_1367,(0,2):C.GC_1115,(0,5):C.GC_2663,(0,3):C.GC_2662,(0,4):C.GC_2662,(0,10):C.GC_2625})

V_76 = Vertex(name = 'V_76',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2777})

V_77 = Vertex(name = 'V_77',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2766,(0,9):C.GC_168,(0,7):C.GC_167,(0,8):C.GC_167,(0,0):C.GC_126,(0,11):C.GC_2793,(0,1):C.GC_1376,(0,2):C.GC_1124,(0,5):C.GC_2669,(0,3):C.GC_2668,(0,4):C.GC_2668,(0,10):C.GC_2628})

V_78 = Vertex(name = 'V_78',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2779})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2767,(0,9):C.GC_186,(0,7):C.GC_185,(0,8):C.GC_185,(0,0):C.GC_135,(0,11):C.GC_2794,(0,1):C.GC_1385,(0,2):C.GC_1133,(0,5):C.GC_2675,(0,3):C.GC_2674,(0,4):C.GC_2674,(0,10):C.GC_2631})

V_80 = Vertex(name = 'V_80',
              particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2781})

V_81 = Vertex(name = 'V_81',
              particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2768,(0,9):C.GC_156,(0,7):C.GC_155,(0,8):C.GC_155,(0,0):C.GC_120,(0,11):C.GC_2795,(0,1):C.GC_1394,(0,2):C.GC_1142,(0,5):C.GC_2681,(0,3):C.GC_2680,(0,4):C.GC_2680,(0,10):C.GC_2634})

V_82 = Vertex(name = 'V_82',
              particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2783})

V_83 = Vertex(name = 'V_83',
              particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2769,(0,9):C.GC_174,(0,7):C.GC_173,(0,8):C.GC_173,(0,0):C.GC_129,(0,11):C.GC_2796,(0,1):C.GC_1403,(0,2):C.GC_1151,(0,5):C.GC_2687,(0,3):C.GC_2686,(0,4):C.GC_2686,(0,10):C.GC_2637})

V_84 = Vertex(name = 'V_84',
              particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2785})

V_85 = Vertex(name = 'V_85',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2770,(0,9):C.GC_192,(0,7):C.GC_191,(0,8):C.GC_191,(0,0):C.GC_138,(0,11):C.GC_2797,(0,1):C.GC_1412,(0,2):C.GC_1160,(0,5):C.GC_2693,(0,3):C.GC_2692,(0,4):C.GC_2692,(0,10):C.GC_2640})

V_86 = Vertex(name = 'V_86',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2787})

V_87 = Vertex(name = 'V_87',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2798,(0,9):C.GC_255,(0,7):C.GC_254,(0,8):C.GC_254,(0,0):C.GC_225,(0,11):C.GC_2825,(0,1):C.GC_1341,(0,2):C.GC_1089,(0,5):C.GC_2647,(0,3):C.GC_2646,(0,4):C.GC_2646,(0,10):C.GC_2617})

V_88 = Vertex(name = 'V_88',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2807})

V_89 = Vertex(name = 'V_89',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2799,(0,9):C.GC_273,(0,7):C.GC_272,(0,8):C.GC_272,(0,0):C.GC_234,(0,11):C.GC_2826,(0,1):C.GC_1350,(0,2):C.GC_1098,(0,5):C.GC_2653,(0,3):C.GC_2652,(0,4):C.GC_2652,(0,10):C.GC_2620})

V_90 = Vertex(name = 'V_90',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2809})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2800,(0,9):C.GC_291,(0,7):C.GC_290,(0,8):C.GC_290,(0,0):C.GC_243,(0,11):C.GC_2827,(0,1):C.GC_1359,(0,2):C.GC_1107,(0,5):C.GC_2659,(0,3):C.GC_2658,(0,4):C.GC_2658,(0,10):C.GC_2623})

V_92 = Vertex(name = 'V_92',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2811})

V_93 = Vertex(name = 'V_93',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2801,(0,9):C.GC_261,(0,7):C.GC_260,(0,8):C.GC_260,(0,0):C.GC_228,(0,11):C.GC_2828,(0,1):C.GC_1368,(0,2):C.GC_1116,(0,5):C.GC_2665,(0,3):C.GC_2664,(0,4):C.GC_2664,(0,10):C.GC_2626})

V_94 = Vertex(name = 'V_94',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2813})

V_95 = Vertex(name = 'V_95',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2802,(0,9):C.GC_279,(0,7):C.GC_278,(0,8):C.GC_278,(0,0):C.GC_237,(0,11):C.GC_2829,(0,1):C.GC_1377,(0,2):C.GC_1125,(0,5):C.GC_2671,(0,3):C.GC_2670,(0,4):C.GC_2670,(0,10):C.GC_2629})

V_96 = Vertex(name = 'V_96',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2815})

V_97 = Vertex(name = 'V_97',
              particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2803,(0,9):C.GC_297,(0,7):C.GC_296,(0,8):C.GC_296,(0,0):C.GC_246,(0,11):C.GC_2830,(0,1):C.GC_1386,(0,2):C.GC_1134,(0,5):C.GC_2677,(0,3):C.GC_2676,(0,4):C.GC_2676,(0,10):C.GC_2632})

V_98 = Vertex(name = 'V_98',
              particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_2817})

V_99 = Vertex(name = 'V_99',
              particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2804,(0,9):C.GC_267,(0,7):C.GC_266,(0,8):C.GC_266,(0,0):C.GC_231,(0,11):C.GC_2831,(0,1):C.GC_1395,(0,2):C.GC_1143,(0,5):C.GC_2683,(0,3):C.GC_2682,(0,4):C.GC_2682,(0,10):C.GC_2635})

V_100 = Vertex(name = 'V_100',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2819})

V_101 = Vertex(name = 'V_101',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2805,(0,9):C.GC_285,(0,7):C.GC_284,(0,8):C.GC_284,(0,0):C.GC_240,(0,11):C.GC_2832,(0,1):C.GC_1404,(0,2):C.GC_1152,(0,5):C.GC_2689,(0,3):C.GC_2688,(0,4):C.GC_2688,(0,10):C.GC_2638})

V_102 = Vertex(name = 'V_102',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2821})

V_103 = Vertex(name = 'V_103',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2806,(0,9):C.GC_303,(0,7):C.GC_302,(0,8):C.GC_302,(0,0):C.GC_249,(0,11):C.GC_2833,(0,1):C.GC_1413,(0,2):C.GC_1161,(0,5):C.GC_2695,(0,3):C.GC_2694,(0,4):C.GC_2694,(0,10):C.GC_2641})

V_104 = Vertex(name = 'V_104',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2823})

V_105 = Vertex(name = 'V_105',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2726,(0,9):C.GC_33,(0,7):C.GC_32,(0,8):C.GC_32,(0,0):C.GC_3,(0,11):C.GC_2753,(0,1):C.GC_1339,(0,2):C.GC_1087,(0,5):C.GC_2643,(0,3):C.GC_2642,(0,4):C.GC_2642,(0,10):C.GC_2615})

V_106 = Vertex(name = 'V_106',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2735})

V_107 = Vertex(name = 'V_107',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2727,(0,9):C.GC_51,(0,7):C.GC_50,(0,8):C.GC_50,(0,0):C.GC_12,(0,11):C.GC_2754,(0,1):C.GC_1348,(0,2):C.GC_1096,(0,5):C.GC_2649,(0,3):C.GC_2648,(0,4):C.GC_2648,(0,10):C.GC_2618})

V_108 = Vertex(name = 'V_108',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2737})

V_109 = Vertex(name = 'V_109',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2728,(0,9):C.GC_69,(0,7):C.GC_68,(0,8):C.GC_68,(0,0):C.GC_21,(0,11):C.GC_2755,(0,1):C.GC_1357,(0,2):C.GC_1105,(0,5):C.GC_2655,(0,3):C.GC_2654,(0,4):C.GC_2654,(0,10):C.GC_2621})

V_110 = Vertex(name = 'V_110',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2739})

V_111 = Vertex(name = 'V_111',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2729,(0,9):C.GC_39,(0,7):C.GC_38,(0,8):C.GC_38,(0,0):C.GC_6,(0,11):C.GC_2756,(0,1):C.GC_1366,(0,2):C.GC_1114,(0,5):C.GC_2661,(0,3):C.GC_2660,(0,4):C.GC_2660,(0,10):C.GC_2624})

V_112 = Vertex(name = 'V_112',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2741})

V_113 = Vertex(name = 'V_113',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2730,(0,9):C.GC_57,(0,7):C.GC_56,(0,8):C.GC_56,(0,0):C.GC_15,(0,11):C.GC_2757,(0,1):C.GC_1375,(0,2):C.GC_1123,(0,5):C.GC_2667,(0,3):C.GC_2666,(0,4):C.GC_2666,(0,10):C.GC_2627})

V_114 = Vertex(name = 'V_114',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2743})

V_115 = Vertex(name = 'V_115',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2731,(0,9):C.GC_75,(0,7):C.GC_74,(0,8):C.GC_74,(0,0):C.GC_24,(0,11):C.GC_2758,(0,1):C.GC_1384,(0,2):C.GC_1132,(0,5):C.GC_2673,(0,3):C.GC_2672,(0,4):C.GC_2672,(0,10):C.GC_2630})

V_116 = Vertex(name = 'V_116',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2745})

V_117 = Vertex(name = 'V_117',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2732,(0,9):C.GC_45,(0,7):C.GC_44,(0,8):C.GC_44,(0,0):C.GC_9,(0,11):C.GC_2759,(0,1):C.GC_1393,(0,2):C.GC_1141,(0,5):C.GC_2679,(0,3):C.GC_2678,(0,4):C.GC_2678,(0,10):C.GC_2633})

V_118 = Vertex(name = 'V_118',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2747})

V_119 = Vertex(name = 'V_119',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2733,(0,9):C.GC_63,(0,7):C.GC_62,(0,8):C.GC_62,(0,0):C.GC_18,(0,11):C.GC_2760,(0,1):C.GC_1402,(0,2):C.GC_1150,(0,5):C.GC_2685,(0,3):C.GC_2684,(0,4):C.GC_2684,(0,10):C.GC_2636})

V_120 = Vertex(name = 'V_120',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2749})

V_121 = Vertex(name = 'V_121',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2734,(0,9):C.GC_81,(0,7):C.GC_80,(0,8):C.GC_80,(0,0):C.GC_27,(0,11):C.GC_2761,(0,1):C.GC_1411,(0,2):C.GC_1159,(0,5):C.GC_2691,(0,3):C.GC_2690,(0,4):C.GC_2690,(0,10):C.GC_2639})

V_122 = Vertex(name = 'V_122',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2751})

V_123 = Vertex(name = 'V_123',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2160,(0,9):C.GC_140,(0,7):C.GC_139,(0,8):C.GC_139,(0,0):C.GC_112,(0,11):C.GC_2187,(0,1):C.GC_1334,(0,2):C.GC_1082,(0,5):C.GC_2043,(0,3):C.GC_2042,(0,4):C.GC_2042,(0,10):C.GC_2014})

V_124 = Vertex(name = 'V_124',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2169})

V_125 = Vertex(name = 'V_125',
               particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2161,(0,9):C.GC_158,(0,7):C.GC_157,(0,8):C.GC_157,(0,0):C.GC_121,(0,11):C.GC_2188,(0,1):C.GC_1343,(0,2):C.GC_1091,(0,5):C.GC_2049,(0,3):C.GC_2048,(0,4):C.GC_2048,(0,10):C.GC_2017})

V_126 = Vertex(name = 'V_126',
               particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2171})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2162,(0,9):C.GC_176,(0,7):C.GC_175,(0,8):C.GC_175,(0,0):C.GC_130,(0,11):C.GC_2189,(0,1):C.GC_1352,(0,2):C.GC_1100,(0,5):C.GC_2055,(0,3):C.GC_2054,(0,4):C.GC_2054,(0,10):C.GC_2020})

V_128 = Vertex(name = 'V_128',
               particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2173})

V_129 = Vertex(name = 'V_129',
               particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2163,(0,9):C.GC_146,(0,7):C.GC_145,(0,8):C.GC_145,(0,0):C.GC_115,(0,11):C.GC_2190,(0,1):C.GC_1361,(0,2):C.GC_1109,(0,5):C.GC_2061,(0,3):C.GC_2060,(0,4):C.GC_2060,(0,10):C.GC_2023})

V_130 = Vertex(name = 'V_130',
               particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2175})

V_131 = Vertex(name = 'V_131',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2164,(0,9):C.GC_164,(0,7):C.GC_163,(0,8):C.GC_163,(0,0):C.GC_124,(0,11):C.GC_2191,(0,1):C.GC_1370,(0,2):C.GC_1118,(0,5):C.GC_2067,(0,3):C.GC_2066,(0,4):C.GC_2066,(0,10):C.GC_2026})

V_132 = Vertex(name = 'V_132',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2177})

V_133 = Vertex(name = 'V_133',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2165,(0,9):C.GC_182,(0,7):C.GC_181,(0,8):C.GC_181,(0,0):C.GC_133,(0,11):C.GC_2192,(0,1):C.GC_1379,(0,2):C.GC_1127,(0,5):C.GC_2073,(0,3):C.GC_2072,(0,4):C.GC_2072,(0,10):C.GC_2029})

V_134 = Vertex(name = 'V_134',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2179})

V_135 = Vertex(name = 'V_135',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2166,(0,9):C.GC_152,(0,7):C.GC_151,(0,8):C.GC_151,(0,0):C.GC_118,(0,11):C.GC_2193,(0,1):C.GC_1388,(0,2):C.GC_1136,(0,5):C.GC_2079,(0,3):C.GC_2078,(0,4):C.GC_2078,(0,10):C.GC_2032})

V_136 = Vertex(name = 'V_136',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2181})

V_137 = Vertex(name = 'V_137',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2167,(0,9):C.GC_170,(0,7):C.GC_169,(0,8):C.GC_169,(0,0):C.GC_127,(0,11):C.GC_2194,(0,1):C.GC_1397,(0,2):C.GC_1145,(0,5):C.GC_2085,(0,3):C.GC_2084,(0,4):C.GC_2084,(0,10):C.GC_2035})

V_138 = Vertex(name = 'V_138',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2183})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2168,(0,9):C.GC_188,(0,7):C.GC_187,(0,8):C.GC_187,(0,0):C.GC_136,(0,11):C.GC_2195,(0,1):C.GC_1406,(0,2):C.GC_1154,(0,5):C.GC_2091,(0,3):C.GC_2090,(0,4):C.GC_2090,(0,10):C.GC_2038})

V_140 = Vertex(name = 'V_140',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2185})

V_141 = Vertex(name = 'V_141',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2196,(0,9):C.GC_251,(0,7):C.GC_250,(0,8):C.GC_250,(0,0):C.GC_223,(0,11):C.GC_2223,(0,1):C.GC_1335,(0,2):C.GC_1083,(0,5):C.GC_2045,(0,3):C.GC_2044,(0,4):C.GC_2044,(0,10):C.GC_2015})

V_142 = Vertex(name = 'V_142',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2205})

V_143 = Vertex(name = 'V_143',
               particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2197,(0,9):C.GC_269,(0,7):C.GC_268,(0,8):C.GC_268,(0,0):C.GC_232,(0,11):C.GC_2224,(0,1):C.GC_1344,(0,2):C.GC_1092,(0,5):C.GC_2051,(0,3):C.GC_2050,(0,4):C.GC_2050,(0,10):C.GC_2018})

V_144 = Vertex(name = 'V_144',
               particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2207})

V_145 = Vertex(name = 'V_145',
               particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2198,(0,9):C.GC_287,(0,7):C.GC_286,(0,8):C.GC_286,(0,0):C.GC_241,(0,11):C.GC_2225,(0,1):C.GC_1353,(0,2):C.GC_1101,(0,5):C.GC_2057,(0,3):C.GC_2056,(0,4):C.GC_2056,(0,10):C.GC_2021})

V_146 = Vertex(name = 'V_146',
               particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2209})

V_147 = Vertex(name = 'V_147',
               particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2199,(0,9):C.GC_257,(0,7):C.GC_256,(0,8):C.GC_256,(0,0):C.GC_226,(0,11):C.GC_2226,(0,1):C.GC_1362,(0,2):C.GC_1110,(0,5):C.GC_2063,(0,3):C.GC_2062,(0,4):C.GC_2062,(0,10):C.GC_2024})

V_148 = Vertex(name = 'V_148',
               particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2211})

V_149 = Vertex(name = 'V_149',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2200,(0,9):C.GC_275,(0,7):C.GC_274,(0,8):C.GC_274,(0,0):C.GC_235,(0,11):C.GC_2227,(0,1):C.GC_1371,(0,2):C.GC_1119,(0,5):C.GC_2069,(0,3):C.GC_2068,(0,4):C.GC_2068,(0,10):C.GC_2027})

V_150 = Vertex(name = 'V_150',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2213})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2201,(0,9):C.GC_293,(0,7):C.GC_292,(0,8):C.GC_292,(0,0):C.GC_244,(0,11):C.GC_2228,(0,1):C.GC_1380,(0,2):C.GC_1128,(0,5):C.GC_2075,(0,3):C.GC_2074,(0,4):C.GC_2074,(0,10):C.GC_2030})

V_152 = Vertex(name = 'V_152',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2215})

V_153 = Vertex(name = 'V_153',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2202,(0,9):C.GC_263,(0,7):C.GC_262,(0,8):C.GC_262,(0,0):C.GC_229,(0,11):C.GC_2229,(0,1):C.GC_1389,(0,2):C.GC_1137,(0,5):C.GC_2081,(0,3):C.GC_2080,(0,4):C.GC_2080,(0,10):C.GC_2033})

V_154 = Vertex(name = 'V_154',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2217})

V_155 = Vertex(name = 'V_155',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2203,(0,9):C.GC_281,(0,7):C.GC_280,(0,8):C.GC_280,(0,0):C.GC_238,(0,11):C.GC_2230,(0,1):C.GC_1398,(0,2):C.GC_1146,(0,5):C.GC_2087,(0,3):C.GC_2086,(0,4):C.GC_2086,(0,10):C.GC_2036})

V_156 = Vertex(name = 'V_156',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2219})

V_157 = Vertex(name = 'V_157',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2204,(0,9):C.GC_299,(0,7):C.GC_298,(0,8):C.GC_298,(0,0):C.GC_247,(0,11):C.GC_2231,(0,1):C.GC_1407,(0,2):C.GC_1155,(0,5):C.GC_2093,(0,3):C.GC_2092,(0,4):C.GC_2092,(0,10):C.GC_2039})

V_158 = Vertex(name = 'V_158',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2221})

V_159 = Vertex(name = 'V_159',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2124,(0,9):C.GC_29,(0,7):C.GC_28,(0,8):C.GC_28,(0,0):C.GC_1,(0,11):C.GC_2151,(0,1):C.GC_1333,(0,2):C.GC_1081,(0,5):C.GC_2041,(0,3):C.GC_2040,(0,4):C.GC_2040,(0,10):C.GC_2013})

V_160 = Vertex(name = 'V_160',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2133})

V_161 = Vertex(name = 'V_161',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2125,(0,9):C.GC_47,(0,7):C.GC_46,(0,8):C.GC_46,(0,0):C.GC_10,(0,11):C.GC_2152,(0,1):C.GC_1342,(0,2):C.GC_1090,(0,5):C.GC_2047,(0,3):C.GC_2046,(0,4):C.GC_2046,(0,10):C.GC_2016})

V_162 = Vertex(name = 'V_162',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2135})

V_163 = Vertex(name = 'V_163',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2126,(0,9):C.GC_65,(0,7):C.GC_64,(0,8):C.GC_64,(0,0):C.GC_19,(0,11):C.GC_2153,(0,1):C.GC_1351,(0,2):C.GC_1099,(0,5):C.GC_2053,(0,3):C.GC_2052,(0,4):C.GC_2052,(0,10):C.GC_2019})

V_164 = Vertex(name = 'V_164',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2137})

V_165 = Vertex(name = 'V_165',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2127,(0,9):C.GC_35,(0,7):C.GC_34,(0,8):C.GC_34,(0,0):C.GC_4,(0,11):C.GC_2154,(0,1):C.GC_1360,(0,2):C.GC_1108,(0,5):C.GC_2059,(0,3):C.GC_2058,(0,4):C.GC_2058,(0,10):C.GC_2022})

V_166 = Vertex(name = 'V_166',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2139})

V_167 = Vertex(name = 'V_167',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2128,(0,9):C.GC_53,(0,7):C.GC_52,(0,8):C.GC_52,(0,0):C.GC_13,(0,3):C.GC_2064,(0,4):C.GC_2064,(0,11):C.GC_2155,(0,1):C.GC_1369,(0,2):C.GC_1117,(0,5):C.GC_2065,(0,10):C.GC_2025})

V_168 = Vertex(name = 'V_168',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2141})

V_169 = Vertex(name = 'V_169',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2129,(0,9):C.GC_71,(0,7):C.GC_70,(0,8):C.GC_70,(0,0):C.GC_22,(0,11):C.GC_2156,(0,1):C.GC_1378,(0,2):C.GC_1126,(0,5):C.GC_2071,(0,3):C.GC_2070,(0,4):C.GC_2070,(0,10):C.GC_2028})

V_170 = Vertex(name = 'V_170',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2143})

V_171 = Vertex(name = 'V_171',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2130,(0,9):C.GC_41,(0,7):C.GC_40,(0,8):C.GC_40,(0,0):C.GC_7,(0,11):C.GC_2157,(0,1):C.GC_1387,(0,2):C.GC_1135,(0,5):C.GC_2077,(0,3):C.GC_2076,(0,4):C.GC_2076,(0,10):C.GC_2031})

V_172 = Vertex(name = 'V_172',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2145})

V_173 = Vertex(name = 'V_173',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2131,(0,9):C.GC_59,(0,7):C.GC_58,(0,8):C.GC_58,(0,0):C.GC_16,(0,11):C.GC_2158,(0,1):C.GC_1396,(0,2):C.GC_1144,(0,5):C.GC_2083,(0,3):C.GC_2082,(0,4):C.GC_2082,(0,10):C.GC_2034})

V_174 = Vertex(name = 'V_174',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2147})

V_175 = Vertex(name = 'V_175',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
               couplings = {(0,6):C.GC_2132,(0,9):C.GC_77,(0,7):C.GC_76,(0,8):C.GC_76,(0,0):C.GC_25,(0,11):C.GC_2159,(0,1):C.GC_1405,(0,2):C.GC_1153,(0,5):C.GC_2089,(0,3):C.GC_2088,(0,4):C.GC_2088,(0,10):C.GC_2037})

V_176 = Vertex(name = 'V_176',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2149})

V_177 = Vertex(name = 'V_177',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2397,(0,4):C.GC_610,(0,2):C.GC_609,(0,3):C.GC_609,(0,0):C.GC_440,(0,5):C.GC_2535})

V_178 = Vertex(name = 'V_178',
               particles = [ P.d__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2395,(0,4):C.GC_598,(0,2):C.GC_597,(0,3):C.GC_597,(0,0):C.GC_434,(0,5):C.GC_2533})

V_179 = Vertex(name = 'V_179',
               particles = [ P.s__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2396,(0,4):C.GC_604,(0,2):C.GC_603,(0,3):C.GC_603,(0,0):C.GC_437,(0,5):C.GC_2534})

V_180 = Vertex(name = 'V_180',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2400,(0,4):C.GC_664,(0,2):C.GC_663,(0,3):C.GC_663,(0,0):C.GC_467,(0,5):C.GC_2544})

V_181 = Vertex(name = 'V_181',
               particles = [ P.d__tilde__, P.c, P.vm__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2398,(0,4):C.GC_652,(0,2):C.GC_651,(0,3):C.GC_651,(0,0):C.GC_461,(0,5):C.GC_2542})

V_182 = Vertex(name = 'V_182',
               particles = [ P.s__tilde__, P.c, P.vm__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2399,(0,4):C.GC_658,(0,2):C.GC_657,(0,3):C.GC_657,(0,0):C.GC_464,(0,5):C.GC_2543})

V_183 = Vertex(name = 'V_183',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2403,(0,4):C.GC_718,(0,2):C.GC_717,(0,3):C.GC_717,(0,0):C.GC_494,(0,5):C.GC_2553})

V_184 = Vertex(name = 'V_184',
               particles = [ P.d__tilde__, P.c, P.vt__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2401,(0,4):C.GC_706,(0,2):C.GC_705,(0,3):C.GC_705,(0,0):C.GC_488,(0,5):C.GC_2551})

V_185 = Vertex(name = 'V_185',
               particles = [ P.s__tilde__, P.c, P.vt__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2402,(0,4):C.GC_712,(0,2):C.GC_711,(0,3):C.GC_711,(0,0):C.GC_491,(0,5):C.GC_2552})

V_186 = Vertex(name = 'V_186',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2406,(0,4):C.GC_628,(0,2):C.GC_627,(0,3):C.GC_627,(0,0):C.GC_449,(0,5):C.GC_2538})

V_187 = Vertex(name = 'V_187',
               particles = [ P.d__tilde__, P.c, P.ve__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2404,(0,4):C.GC_616,(0,2):C.GC_615,(0,3):C.GC_615,(0,0):C.GC_443,(0,5):C.GC_2536})

V_188 = Vertex(name = 'V_188',
               particles = [ P.s__tilde__, P.c, P.ve__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2405,(0,4):C.GC_622,(0,2):C.GC_621,(0,3):C.GC_621,(0,0):C.GC_446,(0,5):C.GC_2537})

V_189 = Vertex(name = 'V_189',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2409,(0,4):C.GC_682,(0,2):C.GC_681,(0,3):C.GC_681,(0,0):C.GC_476,(0,5):C.GC_2547})

V_190 = Vertex(name = 'V_190',
               particles = [ P.d__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2407,(0,4):C.GC_670,(0,2):C.GC_669,(0,3):C.GC_669,(0,0):C.GC_470,(0,5):C.GC_2545})

V_191 = Vertex(name = 'V_191',
               particles = [ P.s__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2408,(0,4):C.GC_676,(0,2):C.GC_675,(0,3):C.GC_675,(0,0):C.GC_473,(0,5):C.GC_2546})

V_192 = Vertex(name = 'V_192',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2412,(0,4):C.GC_736,(0,2):C.GC_735,(0,3):C.GC_735,(0,0):C.GC_503,(0,5):C.GC_2556})

V_193 = Vertex(name = 'V_193',
               particles = [ P.d__tilde__, P.c, P.vt__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2410,(0,4):C.GC_724,(0,2):C.GC_723,(0,3):C.GC_723,(0,0):C.GC_497,(0,5):C.GC_2554})

V_194 = Vertex(name = 'V_194',
               particles = [ P.s__tilde__, P.c, P.vt__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2411,(0,4):C.GC_730,(0,2):C.GC_729,(0,3):C.GC_729,(0,0):C.GC_500,(0,5):C.GC_2555})

V_195 = Vertex(name = 'V_195',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2415,(0,4):C.GC_646,(0,2):C.GC_645,(0,3):C.GC_645,(0,0):C.GC_458,(0,5):C.GC_2541})

V_196 = Vertex(name = 'V_196',
               particles = [ P.d__tilde__, P.c, P.ve__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2413,(0,4):C.GC_634,(0,2):C.GC_633,(0,3):C.GC_633,(0,0):C.GC_452,(0,5):C.GC_2539})

V_197 = Vertex(name = 'V_197',
               particles = [ P.s__tilde__, P.c, P.ve__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2414,(0,4):C.GC_640,(0,2):C.GC_639,(0,3):C.GC_639,(0,0):C.GC_455,(0,5):C.GC_2540})

V_198 = Vertex(name = 'V_198',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2418,(0,4):C.GC_700,(0,2):C.GC_699,(0,3):C.GC_699,(0,0):C.GC_485,(0,5):C.GC_2550})

V_199 = Vertex(name = 'V_199',
               particles = [ P.d__tilde__, P.c, P.vm__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2416,(0,4):C.GC_688,(0,2):C.GC_687,(0,3):C.GC_687,(0,0):C.GC_479,(0,5):C.GC_2548})

V_200 = Vertex(name = 'V_200',
               particles = [ P.s__tilde__, P.c, P.vm__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2417,(0,4):C.GC_694,(0,2):C.GC_693,(0,3):C.GC_693,(0,0):C.GC_482,(0,5):C.GC_2549})

V_201 = Vertex(name = 'V_201',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2421,(0,4):C.GC_754,(0,2):C.GC_753,(0,3):C.GC_753,(0,0):C.GC_512,(0,5):C.GC_2559})

V_202 = Vertex(name = 'V_202',
               particles = [ P.d__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2419,(0,4):C.GC_742,(0,2):C.GC_741,(0,3):C.GC_741,(0,0):C.GC_506,(0,5):C.GC_2557})

V_203 = Vertex(name = 'V_203',
               particles = [ P.s__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(0,1):C.GC_2420,(0,4):C.GC_748,(0,2):C.GC_747,(0,3):C.GC_747,(0,0):C.GC_509,(0,5):C.GC_2558})

V_204 = Vertex(name = 'V_204',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2698,(0,4):C.GC_612,(0,2):C.GC_611,(0,3):C.GC_611,(0,0):C.GC_441,(0,5):C.GC_2836})

V_205 = Vertex(name = 'V_205',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2701,(0,4):C.GC_666,(0,2):C.GC_665,(0,3):C.GC_665,(0,0):C.GC_468,(0,5):C.GC_2845})

V_206 = Vertex(name = 'V_206',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2704,(0,4):C.GC_720,(0,2):C.GC_719,(0,3):C.GC_719,(0,0):C.GC_495,(0,5):C.GC_2854})

V_207 = Vertex(name = 'V_207',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2707,(0,4):C.GC_630,(0,2):C.GC_629,(0,3):C.GC_629,(0,0):C.GC_450,(0,5):C.GC_2839})

V_208 = Vertex(name = 'V_208',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2710,(0,4):C.GC_684,(0,2):C.GC_683,(0,3):C.GC_683,(0,0):C.GC_477,(0,5):C.GC_2848})

V_209 = Vertex(name = 'V_209',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2713,(0,4):C.GC_738,(0,2):C.GC_737,(0,3):C.GC_737,(0,0):C.GC_504,(0,5):C.GC_2857})

V_210 = Vertex(name = 'V_210',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2716,(0,4):C.GC_648,(0,2):C.GC_647,(0,3):C.GC_647,(0,0):C.GC_459,(0,5):C.GC_2842})

V_211 = Vertex(name = 'V_211',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2719,(0,4):C.GC_702,(0,2):C.GC_701,(0,3):C.GC_701,(0,0):C.GC_486,(0,5):C.GC_2851})

V_212 = Vertex(name = 'V_212',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2722,(0,4):C.GC_756,(0,2):C.GC_755,(0,3):C.GC_755,(0,0):C.GC_513,(0,5):C.GC_2860})

V_213 = Vertex(name = 'V_213',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2696,(0,4):C.GC_600,(0,2):C.GC_599,(0,3):C.GC_599,(0,0):C.GC_435,(0,5):C.GC_2834})

V_214 = Vertex(name = 'V_214',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2699,(0,4):C.GC_654,(0,2):C.GC_653,(0,3):C.GC_653,(0,0):C.GC_462,(0,5):C.GC_2843})

V_215 = Vertex(name = 'V_215',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2702,(0,4):C.GC_708,(0,2):C.GC_707,(0,3):C.GC_707,(0,0):C.GC_489,(0,5):C.GC_2852})

V_216 = Vertex(name = 'V_216',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2705,(0,4):C.GC_618,(0,2):C.GC_617,(0,3):C.GC_617,(0,0):C.GC_444,(0,5):C.GC_2837})

V_217 = Vertex(name = 'V_217',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2708,(0,4):C.GC_672,(0,2):C.GC_671,(0,3):C.GC_671,(0,0):C.GC_471,(0,5):C.GC_2846})

V_218 = Vertex(name = 'V_218',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2711,(0,4):C.GC_726,(0,2):C.GC_725,(0,3):C.GC_725,(0,0):C.GC_498,(0,5):C.GC_2855})

V_219 = Vertex(name = 'V_219',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2714,(0,4):C.GC_636,(0,2):C.GC_635,(0,3):C.GC_635,(0,0):C.GC_453,(0,5):C.GC_2840})

V_220 = Vertex(name = 'V_220',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2717,(0,4):C.GC_690,(0,2):C.GC_689,(0,3):C.GC_689,(0,0):C.GC_480,(0,5):C.GC_2849})

V_221 = Vertex(name = 'V_221',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2720,(0,4):C.GC_744,(0,2):C.GC_743,(0,3):C.GC_743,(0,0):C.GC_507,(0,5):C.GC_2858})

V_222 = Vertex(name = 'V_222',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2697,(0,4):C.GC_606,(0,2):C.GC_605,(0,3):C.GC_605,(0,0):C.GC_438,(0,5):C.GC_2835})

V_223 = Vertex(name = 'V_223',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2700,(0,4):C.GC_660,(0,2):C.GC_659,(0,3):C.GC_659,(0,0):C.GC_465,(0,5):C.GC_2844})

V_224 = Vertex(name = 'V_224',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2703,(0,4):C.GC_714,(0,2):C.GC_713,(0,3):C.GC_713,(0,0):C.GC_492,(0,5):C.GC_2853})

V_225 = Vertex(name = 'V_225',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2706,(0,4):C.GC_624,(0,2):C.GC_623,(0,3):C.GC_623,(0,0):C.GC_447,(0,5):C.GC_2838})

V_226 = Vertex(name = 'V_226',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2709,(0,4):C.GC_678,(0,2):C.GC_677,(0,3):C.GC_677,(0,0):C.GC_474,(0,5):C.GC_2847})

V_227 = Vertex(name = 'V_227',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2712,(0,4):C.GC_732,(0,2):C.GC_731,(0,3):C.GC_731,(0,0):C.GC_501,(0,5):C.GC_2856})

V_228 = Vertex(name = 'V_228',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2715,(0,4):C.GC_642,(0,2):C.GC_641,(0,3):C.GC_641,(0,0):C.GC_456,(0,5):C.GC_2841})

V_229 = Vertex(name = 'V_229',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2718,(0,4):C.GC_696,(0,2):C.GC_695,(0,3):C.GC_695,(0,0):C.GC_483,(0,5):C.GC_2850})

V_230 = Vertex(name = 'V_230',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2721,(0,4):C.GC_750,(0,2):C.GC_749,(0,3):C.GC_749,(0,0):C.GC_510,(0,5):C.GC_2859})

V_231 = Vertex(name = 'V_231',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2096,(0,4):C.GC_608,(0,2):C.GC_607,(0,3):C.GC_607,(0,0):C.GC_439,(0,5):C.GC_2234})

V_232 = Vertex(name = 'V_232',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2099,(0,4):C.GC_662,(0,2):C.GC_661,(0,3):C.GC_661,(0,0):C.GC_466,(0,5):C.GC_2243})

V_233 = Vertex(name = 'V_233',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2102,(0,4):C.GC_716,(0,2):C.GC_715,(0,3):C.GC_715,(0,0):C.GC_493,(0,5):C.GC_2252})

V_234 = Vertex(name = 'V_234',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2105,(0,4):C.GC_626,(0,2):C.GC_625,(0,3):C.GC_625,(0,0):C.GC_448,(0,5):C.GC_2237})

V_235 = Vertex(name = 'V_235',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2108,(0,4):C.GC_680,(0,2):C.GC_679,(0,3):C.GC_679,(0,0):C.GC_475,(0,5):C.GC_2246})

V_236 = Vertex(name = 'V_236',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2111,(0,4):C.GC_734,(0,2):C.GC_733,(0,3):C.GC_733,(0,0):C.GC_502,(0,5):C.GC_2255})

V_237 = Vertex(name = 'V_237',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2114,(0,4):C.GC_644,(0,2):C.GC_643,(0,3):C.GC_643,(0,0):C.GC_457,(0,5):C.GC_2240})

V_238 = Vertex(name = 'V_238',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2117,(0,4):C.GC_698,(0,2):C.GC_697,(0,3):C.GC_697,(0,0):C.GC_484,(0,5):C.GC_2249})

V_239 = Vertex(name = 'V_239',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2120,(0,4):C.GC_752,(0,2):C.GC_751,(0,3):C.GC_751,(0,0):C.GC_511,(0,5):C.GC_2258})

V_240 = Vertex(name = 'V_240',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2094,(0,4):C.GC_596,(0,2):C.GC_595,(0,3):C.GC_595,(0,0):C.GC_433,(0,5):C.GC_2232})

V_241 = Vertex(name = 'V_241',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2097,(0,4):C.GC_650,(0,2):C.GC_649,(0,3):C.GC_649,(0,0):C.GC_460,(0,5):C.GC_2241})

V_242 = Vertex(name = 'V_242',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2100,(0,4):C.GC_704,(0,2):C.GC_703,(0,3):C.GC_703,(0,0):C.GC_487,(0,5):C.GC_2250})

V_243 = Vertex(name = 'V_243',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2103,(0,4):C.GC_614,(0,2):C.GC_613,(0,3):C.GC_613,(0,0):C.GC_442,(0,5):C.GC_2235})

V_244 = Vertex(name = 'V_244',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2106,(0,4):C.GC_668,(0,2):C.GC_667,(0,3):C.GC_667,(0,0):C.GC_469,(0,5):C.GC_2244})

V_245 = Vertex(name = 'V_245',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2109,(0,4):C.GC_722,(0,2):C.GC_721,(0,3):C.GC_721,(0,0):C.GC_496,(0,5):C.GC_2253})

V_246 = Vertex(name = 'V_246',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2112,(0,4):C.GC_632,(0,2):C.GC_631,(0,3):C.GC_631,(0,0):C.GC_451,(0,5):C.GC_2238})

V_247 = Vertex(name = 'V_247',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2115,(0,4):C.GC_686,(0,2):C.GC_685,(0,3):C.GC_685,(0,0):C.GC_478,(0,5):C.GC_2247})

V_248 = Vertex(name = 'V_248',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2118,(0,4):C.GC_740,(0,2):C.GC_739,(0,3):C.GC_739,(0,0):C.GC_505,(0,5):C.GC_2256})

V_249 = Vertex(name = 'V_249',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2095,(0,4):C.GC_602,(0,2):C.GC_601,(0,3):C.GC_601,(0,0):C.GC_436,(0,5):C.GC_2233})

V_250 = Vertex(name = 'V_250',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2098,(0,4):C.GC_656,(0,2):C.GC_655,(0,3):C.GC_655,(0,0):C.GC_463,(0,5):C.GC_2242})

V_251 = Vertex(name = 'V_251',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2101,(0,4):C.GC_710,(0,2):C.GC_709,(0,3):C.GC_709,(0,0):C.GC_490,(0,5):C.GC_2251})

V_252 = Vertex(name = 'V_252',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2104,(0,4):C.GC_620,(0,2):C.GC_619,(0,3):C.GC_619,(0,0):C.GC_445,(0,5):C.GC_2236})

V_253 = Vertex(name = 'V_253',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2107,(0,4):C.GC_674,(0,2):C.GC_673,(0,3):C.GC_673,(0,0):C.GC_472,(0,5):C.GC_2245})

V_254 = Vertex(name = 'V_254',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2110,(0,4):C.GC_728,(0,2):C.GC_727,(0,3):C.GC_727,(0,0):C.GC_499,(0,5):C.GC_2254})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2113,(0,4):C.GC_638,(0,2):C.GC_637,(0,3):C.GC_637,(0,0):C.GC_454,(0,5):C.GC_2239})

V_256 = Vertex(name = 'V_256',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2116,(0,4):C.GC_692,(0,2):C.GC_691,(0,3):C.GC_691,(0,0):C.GC_481,(0,5):C.GC_2248})

V_257 = Vertex(name = 'V_257',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_2119,(0,4):C.GC_746,(0,2):C.GC_745,(0,3):C.GC_745,(0,0):C.GC_508,(0,5):C.GC_2257})

V_258 = Vertex(name = 'V_258',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_522,(0,5):C.GC_1008,(0,0):C.GC_1179,(0,1):C.GC_927,(0,3):C.GC_1260,(0,4):C.GC_1260})

V_259 = Vertex(name = 'V_259',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_774})

V_260 = Vertex(name = 'V_260',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_520,(0,5):C.GC_1006,(0,0):C.GC_1177,(0,1):C.GC_925,(0,3):C.GC_1258,(0,4):C.GC_1254})

V_261 = Vertex(name = 'V_261',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_770})

V_262 = Vertex(name = 'V_262',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_521,(0,5):C.GC_1007,(0,0):C.GC_1178,(0,1):C.GC_926,(0,3):C.GC_1259,(0,4):C.GC_1257})

V_263 = Vertex(name = 'V_263',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_772})

V_264 = Vertex(name = 'V_264',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_516,(0,5):C.GC_1002,(0,0):C.GC_1173,(0,1):C.GC_921,(0,3):C.GC_1254,(0,4):C.GC_1258})

V_265 = Vertex(name = 'V_265',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_762})

V_266 = Vertex(name = 'V_266',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_514,(0,5):C.GC_1000,(0,0):C.GC_1171,(0,1):C.GC_919,(0,3):C.GC_1252,(0,4):C.GC_1252})

V_267 = Vertex(name = 'V_267',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_758})

V_268 = Vertex(name = 'V_268',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_515,(0,5):C.GC_1001,(0,0):C.GC_1172,(0,1):C.GC_920,(0,3):C.GC_1253,(0,4):C.GC_1255})

V_269 = Vertex(name = 'V_269',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_760})

V_270 = Vertex(name = 'V_270',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_531,(0,5):C.GC_1017,(0,0):C.GC_1188,(0,1):C.GC_936,(0,3):C.GC_1269,(0,4):C.GC_1287})

V_271 = Vertex(name = 'V_271',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_792})

V_272 = Vertex(name = 'V_272',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_529,(0,5):C.GC_1015,(0,0):C.GC_1186,(0,1):C.GC_934,(0,3):C.GC_1267,(0,4):C.GC_1281})

V_273 = Vertex(name = 'V_273',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_788})

V_274 = Vertex(name = 'V_274',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_530,(0,5):C.GC_1016,(0,0):C.GC_1187,(0,1):C.GC_935,(0,3):C.GC_1268,(0,4):C.GC_1284})

V_275 = Vertex(name = 'V_275',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_790})

V_276 = Vertex(name = 'V_276',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_525,(0,5):C.GC_1011,(0,0):C.GC_1182,(0,1):C.GC_930,(0,3):C.GC_1263,(0,4):C.GC_1285})

V_277 = Vertex(name = 'V_277',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_780})

V_278 = Vertex(name = 'V_278',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_523,(0,5):C.GC_1009,(0,0):C.GC_1180,(0,1):C.GC_928,(0,3):C.GC_1261,(0,4):C.GC_1279})

V_279 = Vertex(name = 'V_279',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_776})

V_280 = Vertex(name = 'V_280',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_524,(0,5):C.GC_1010,(0,0):C.GC_1181,(0,1):C.GC_929,(0,3):C.GC_1262,(0,4):C.GC_1282})

V_281 = Vertex(name = 'V_281',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_778})

V_282 = Vertex(name = 'V_282',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_540,(0,5):C.GC_1026,(0,0):C.GC_1197,(0,1):C.GC_945,(0,3):C.GC_1278,(0,4):C.GC_1314})

V_283 = Vertex(name = 'V_283',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_810})

V_284 = Vertex(name = 'V_284',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_538,(0,5):C.GC_1024,(0,0):C.GC_1195,(0,1):C.GC_943,(0,3):C.GC_1276,(0,4):C.GC_1308})

V_285 = Vertex(name = 'V_285',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_806})

V_286 = Vertex(name = 'V_286',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_539,(0,5):C.GC_1025,(0,0):C.GC_1196,(0,1):C.GC_944,(0,3):C.GC_1277,(0,4):C.GC_1311})

V_287 = Vertex(name = 'V_287',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_808})

V_288 = Vertex(name = 'V_288',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_534,(0,5):C.GC_1020,(0,0):C.GC_1191,(0,1):C.GC_939,(0,3):C.GC_1272,(0,4):C.GC_1312})

V_289 = Vertex(name = 'V_289',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_798})

V_290 = Vertex(name = 'V_290',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_532,(0,5):C.GC_1018,(0,0):C.GC_1189,(0,1):C.GC_937,(0,3):C.GC_1270,(0,4):C.GC_1306})

V_291 = Vertex(name = 'V_291',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_794})

V_292 = Vertex(name = 'V_292',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_533,(0,5):C.GC_1019,(0,0):C.GC_1190,(0,1):C.GC_938,(0,3):C.GC_1271,(0,4):C.GC_1309})

V_293 = Vertex(name = 'V_293',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_796})

V_294 = Vertex(name = 'V_294',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_549,(0,5):C.GC_1035,(0,0):C.GC_1206,(0,1):C.GC_954,(0,3):C.GC_1287,(0,4):C.GC_1269})

V_295 = Vertex(name = 'V_295',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_828})

V_296 = Vertex(name = 'V_296',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_547,(0,5):C.GC_1033,(0,0):C.GC_1204,(0,1):C.GC_952,(0,3):C.GC_1285,(0,4):C.GC_1263})

V_297 = Vertex(name = 'V_297',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_824})

V_298 = Vertex(name = 'V_298',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_548,(0,5):C.GC_1034,(0,0):C.GC_1205,(0,1):C.GC_953,(0,3):C.GC_1286,(0,4):C.GC_1266})

V_299 = Vertex(name = 'V_299',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_826})

V_300 = Vertex(name = 'V_300',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_543,(0,5):C.GC_1029,(0,0):C.GC_1200,(0,1):C.GC_948,(0,3):C.GC_1281,(0,4):C.GC_1267})

V_301 = Vertex(name = 'V_301',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_816})

V_302 = Vertex(name = 'V_302',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_541,(0,5):C.GC_1027,(0,0):C.GC_1198,(0,1):C.GC_946,(0,3):C.GC_1279,(0,4):C.GC_1261})

V_303 = Vertex(name = 'V_303',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_812})

V_304 = Vertex(name = 'V_304',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_542,(0,5):C.GC_1028,(0,0):C.GC_1199,(0,1):C.GC_947,(0,3):C.GC_1280,(0,4):C.GC_1264})

V_305 = Vertex(name = 'V_305',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_814})

V_306 = Vertex(name = 'V_306',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_558,(0,5):C.GC_1044,(0,0):C.GC_1215,(0,1):C.GC_963,(0,3):C.GC_1296,(0,4):C.GC_1296})

V_307 = Vertex(name = 'V_307',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_846})

V_308 = Vertex(name = 'V_308',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_556,(0,5):C.GC_1042,(0,0):C.GC_1213,(0,1):C.GC_961,(0,3):C.GC_1294,(0,4):C.GC_1290})

V_309 = Vertex(name = 'V_309',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_842})

V_310 = Vertex(name = 'V_310',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_557,(0,5):C.GC_1043,(0,0):C.GC_1214,(0,1):C.GC_962,(0,3):C.GC_1295,(0,4):C.GC_1293})

V_311 = Vertex(name = 'V_311',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_844})

V_312 = Vertex(name = 'V_312',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_552,(0,5):C.GC_1038,(0,0):C.GC_1209,(0,1):C.GC_957,(0,3):C.GC_1290,(0,4):C.GC_1294})

V_313 = Vertex(name = 'V_313',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_834})

V_314 = Vertex(name = 'V_314',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_550,(0,5):C.GC_1036,(0,0):C.GC_1207,(0,1):C.GC_955,(0,3):C.GC_1288,(0,4):C.GC_1288})

V_315 = Vertex(name = 'V_315',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_830})

V_316 = Vertex(name = 'V_316',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_551,(0,5):C.GC_1037,(0,0):C.GC_1208,(0,1):C.GC_956,(0,3):C.GC_1289,(0,4):C.GC_1291})

V_317 = Vertex(name = 'V_317',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_832})

V_318 = Vertex(name = 'V_318',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_567,(0,5):C.GC_1053,(0,0):C.GC_1224,(0,1):C.GC_972,(0,3):C.GC_1305,(0,4):C.GC_1323})

V_319 = Vertex(name = 'V_319',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_864})

V_320 = Vertex(name = 'V_320',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_565,(0,5):C.GC_1051,(0,0):C.GC_1222,(0,1):C.GC_970,(0,3):C.GC_1303,(0,4):C.GC_1317})

V_321 = Vertex(name = 'V_321',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_860})

V_322 = Vertex(name = 'V_322',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_566,(0,5):C.GC_1052,(0,0):C.GC_1223,(0,1):C.GC_971,(0,3):C.GC_1304,(0,4):C.GC_1320})

V_323 = Vertex(name = 'V_323',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_862})

V_324 = Vertex(name = 'V_324',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_561,(0,5):C.GC_1047,(0,0):C.GC_1218,(0,1):C.GC_966,(0,3):C.GC_1299,(0,4):C.GC_1321})

V_325 = Vertex(name = 'V_325',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_852})

V_326 = Vertex(name = 'V_326',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_559,(0,5):C.GC_1045,(0,0):C.GC_1216,(0,1):C.GC_964,(0,3):C.GC_1297,(0,4):C.GC_1315})

V_327 = Vertex(name = 'V_327',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_848})

V_328 = Vertex(name = 'V_328',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_560,(0,5):C.GC_1046,(0,0):C.GC_1217,(0,1):C.GC_965,(0,3):C.GC_1298,(0,4):C.GC_1318})

V_329 = Vertex(name = 'V_329',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_850})

V_330 = Vertex(name = 'V_330',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_519,(0,5):C.GC_1176,(0,0):C.GC_1005,(0,1):C.GC_924,(0,3):C.GC_1259,(0,4):C.GC_1257})

V_331 = Vertex(name = 'V_331',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_768})

V_332 = Vertex(name = 'V_332',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_528,(0,5):C.GC_1185,(0,0):C.GC_1014,(0,1):C.GC_933,(0,3):C.GC_1286,(0,4):C.GC_1266})

V_333 = Vertex(name = 'V_333',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_786})

V_334 = Vertex(name = 'V_334',
               particles = [ P.b__tilde__, P.s, P.ta__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_537,(0,5):C.GC_1194,(0,0):C.GC_1023,(0,1):C.GC_942,(0,3):C.GC_1313,(0,4):C.GC_1275})

V_335 = Vertex(name = 'V_335',
               particles = [ P.b__tilde__, P.s, P.ta__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_804})

V_336 = Vertex(name = 'V_336',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_546,(0,5):C.GC_1203,(0,0):C.GC_1032,(0,1):C.GC_951,(0,3):C.GC_1268,(0,4):C.GC_1284})

V_337 = Vertex(name = 'V_337',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_822})

V_338 = Vertex(name = 'V_338',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_555,(0,5):C.GC_1212,(0,0):C.GC_1041,(0,1):C.GC_960,(0,3):C.GC_1295,(0,4):C.GC_1293})

V_339 = Vertex(name = 'V_339',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_840})

V_340 = Vertex(name = 'V_340',
               particles = [ P.b__tilde__, P.s, P.ta__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_564,(0,5):C.GC_1221,(0,0):C.GC_1050,(0,1):C.GC_969,(0,3):C.GC_1322,(0,4):C.GC_1302})

V_341 = Vertex(name = 'V_341',
               particles = [ P.b__tilde__, P.s, P.ta__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_858})

V_342 = Vertex(name = 'V_342',
               particles = [ P.d__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_517,(0,5):C.GC_1174,(0,0):C.GC_1003,(0,1):C.GC_922,(0,3):C.GC_1253,(0,4):C.GC_1255})

V_343 = Vertex(name = 'V_343',
               particles = [ P.d__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_764})

V_344 = Vertex(name = 'V_344',
               particles = [ P.d__tilde__, P.s, P.mu__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_526,(0,5):C.GC_1183,(0,0):C.GC_1012,(0,1):C.GC_931,(0,3):C.GC_1280,(0,4):C.GC_1264})

V_345 = Vertex(name = 'V_345',
               particles = [ P.d__tilde__, P.s, P.mu__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_782})

V_346 = Vertex(name = 'V_346',
               particles = [ P.d__tilde__, P.s, P.ta__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_535,(0,5):C.GC_1192,(0,0):C.GC_1021,(0,1):C.GC_940,(0,3):C.GC_1307,(0,4):C.GC_1273})

V_347 = Vertex(name = 'V_347',
               particles = [ P.d__tilde__, P.s, P.ta__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_800})

V_348 = Vertex(name = 'V_348',
               particles = [ P.d__tilde__, P.s, P.e__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_544,(0,5):C.GC_1201,(0,0):C.GC_1030,(0,1):C.GC_949,(0,3):C.GC_1262,(0,4):C.GC_1282})

V_349 = Vertex(name = 'V_349',
               particles = [ P.d__tilde__, P.s, P.e__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_818})

V_350 = Vertex(name = 'V_350',
               particles = [ P.d__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_553,(0,5):C.GC_1210,(0,0):C.GC_1039,(0,1):C.GC_958,(0,3):C.GC_1289,(0,4):C.GC_1291})

V_351 = Vertex(name = 'V_351',
               particles = [ P.d__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_836})

V_352 = Vertex(name = 'V_352',
               particles = [ P.d__tilde__, P.s, P.ta__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_562,(0,5):C.GC_1219,(0,0):C.GC_1048,(0,1):C.GC_967,(0,3):C.GC_1316,(0,4):C.GC_1300})

V_353 = Vertex(name = 'V_353',
               particles = [ P.d__tilde__, P.s, P.ta__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_854})

V_354 = Vertex(name = 'V_354',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_518,(0,5):C.GC_1175,(0,0):C.GC_1004,(0,1):C.GC_923,(0,3):C.GC_1256,(0,4):C.GC_1256})

V_355 = Vertex(name = 'V_355',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_766})

V_356 = Vertex(name = 'V_356',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_527,(0,5):C.GC_1184,(0,0):C.GC_1013,(0,1):C.GC_932,(0,3):C.GC_1283,(0,4):C.GC_1265})

V_357 = Vertex(name = 'V_357',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_784})

V_358 = Vertex(name = 'V_358',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_536,(0,5):C.GC_1193,(0,0):C.GC_1022,(0,1):C.GC_941,(0,3):C.GC_1310,(0,4):C.GC_1274})

V_359 = Vertex(name = 'V_359',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_802})

V_360 = Vertex(name = 'V_360',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_545,(0,5):C.GC_1202,(0,0):C.GC_1031,(0,1):C.GC_950,(0,3):C.GC_1265,(0,4):C.GC_1283})

V_361 = Vertex(name = 'V_361',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_820})

V_362 = Vertex(name = 'V_362',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_554,(0,5):C.GC_1211,(0,0):C.GC_1040,(0,1):C.GC_959,(0,3):C.GC_1292,(0,4):C.GC_1292})

V_363 = Vertex(name = 'V_363',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_838})

V_364 = Vertex(name = 'V_364',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_563,(0,5):C.GC_1220,(0,0):C.GC_1049,(0,1):C.GC_968,(0,3):C.GC_1319,(0,4):C.GC_1301})

V_365 = Vertex(name = 'V_365',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_856})

V_366 = Vertex(name = 'V_366',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_576,(0,5):C.GC_1062,(0,0):C.GC_1233,(0,1):C.GC_981,(0,3):C.GC_1314,(0,4):C.GC_1278})

V_367 = Vertex(name = 'V_367',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_882})

V_368 = Vertex(name = 'V_368',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_574,(0,5):C.GC_1060,(0,0):C.GC_1231,(0,1):C.GC_979,(0,3):C.GC_1312,(0,4):C.GC_1272})

V_369 = Vertex(name = 'V_369',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_878})

V_370 = Vertex(name = 'V_370',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_575,(0,5):C.GC_1061,(0,0):C.GC_1232,(0,1):C.GC_980,(0,3):C.GC_1313,(0,4):C.GC_1275})

V_371 = Vertex(name = 'V_371',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_880})

V_372 = Vertex(name = 'V_372',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_570,(0,5):C.GC_1056,(0,0):C.GC_1227,(0,1):C.GC_975,(0,3):C.GC_1308,(0,4):C.GC_1276})

V_373 = Vertex(name = 'V_373',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_870})

V_374 = Vertex(name = 'V_374',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_568,(0,5):C.GC_1054,(0,0):C.GC_1225,(0,1):C.GC_973,(0,3):C.GC_1306,(0,4):C.GC_1270})

V_375 = Vertex(name = 'V_375',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_866})

V_376 = Vertex(name = 'V_376',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_569,(0,5):C.GC_1055,(0,0):C.GC_1226,(0,1):C.GC_974,(0,3):C.GC_1307,(0,4):C.GC_1273})

V_377 = Vertex(name = 'V_377',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_868})

V_378 = Vertex(name = 'V_378',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_573,(0,5):C.GC_1059,(0,0):C.GC_1230,(0,1):C.GC_978,(0,3):C.GC_1311,(0,4):C.GC_1277})

V_379 = Vertex(name = 'V_379',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_876})

V_380 = Vertex(name = 'V_380',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_571,(0,5):C.GC_1057,(0,0):C.GC_1228,(0,1):C.GC_976,(0,3):C.GC_1309,(0,4):C.GC_1271})

V_381 = Vertex(name = 'V_381',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_872})

V_382 = Vertex(name = 'V_382',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_572,(0,5):C.GC_1058,(0,0):C.GC_1229,(0,1):C.GC_977,(0,3):C.GC_1310,(0,4):C.GC_1274})

V_383 = Vertex(name = 'V_383',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_874})

V_384 = Vertex(name = 'V_384',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_585,(0,5):C.GC_1071,(0,0):C.GC_1242,(0,1):C.GC_990,(0,3):C.GC_1323,(0,4):C.GC_1305})

V_385 = Vertex(name = 'V_385',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_900})

V_386 = Vertex(name = 'V_386',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_583,(0,5):C.GC_1069,(0,0):C.GC_1240,(0,1):C.GC_988,(0,3):C.GC_1321,(0,4):C.GC_1299})

V_387 = Vertex(name = 'V_387',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_896})

V_388 = Vertex(name = 'V_388',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_584,(0,5):C.GC_1070,(0,0):C.GC_1241,(0,1):C.GC_989,(0,3):C.GC_1322,(0,4):C.GC_1302})

V_389 = Vertex(name = 'V_389',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_898})

V_390 = Vertex(name = 'V_390',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_579,(0,5):C.GC_1065,(0,0):C.GC_1236,(0,1):C.GC_984,(0,3):C.GC_1317,(0,4):C.GC_1303})

V_391 = Vertex(name = 'V_391',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_888})

V_392 = Vertex(name = 'V_392',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_577,(0,5):C.GC_1063,(0,0):C.GC_1234,(0,1):C.GC_982,(0,3):C.GC_1315,(0,4):C.GC_1297})

V_393 = Vertex(name = 'V_393',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_884})

V_394 = Vertex(name = 'V_394',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_578,(0,5):C.GC_1064,(0,0):C.GC_1235,(0,1):C.GC_983,(0,3):C.GC_1316,(0,4):C.GC_1300})

V_395 = Vertex(name = 'V_395',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_886})

V_396 = Vertex(name = 'V_396',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_582,(0,5):C.GC_1068,(0,0):C.GC_1239,(0,1):C.GC_987,(0,3):C.GC_1320,(0,4):C.GC_1304})

V_397 = Vertex(name = 'V_397',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_894})

V_398 = Vertex(name = 'V_398',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_580,(0,5):C.GC_1066,(0,0):C.GC_1237,(0,1):C.GC_985,(0,3):C.GC_1318,(0,4):C.GC_1298})

V_399 = Vertex(name = 'V_399',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_890})

V_400 = Vertex(name = 'V_400',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_581,(0,5):C.GC_1067,(0,0):C.GC_1238,(0,1):C.GC_986,(0,3):C.GC_1319,(0,4):C.GC_1301})

V_401 = Vertex(name = 'V_401',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_892})

V_402 = Vertex(name = 'V_402',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_594,(0,5):C.GC_1080,(0,0):C.GC_1251,(0,1):C.GC_999,(0,3):C.GC_1332,(0,4):C.GC_1332})

V_403 = Vertex(name = 'V_403',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_918})

V_404 = Vertex(name = 'V_404',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_592,(0,5):C.GC_1078,(0,0):C.GC_1249,(0,1):C.GC_997,(0,3):C.GC_1330,(0,4):C.GC_1326})

V_405 = Vertex(name = 'V_405',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_914})

V_406 = Vertex(name = 'V_406',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_593,(0,5):C.GC_1079,(0,0):C.GC_1250,(0,1):C.GC_998,(0,3):C.GC_1331,(0,4):C.GC_1329})

V_407 = Vertex(name = 'V_407',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_916})

V_408 = Vertex(name = 'V_408',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_588,(0,5):C.GC_1074,(0,0):C.GC_1245,(0,1):C.GC_993,(0,3):C.GC_1326,(0,4):C.GC_1330})

V_409 = Vertex(name = 'V_409',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_906})

V_410 = Vertex(name = 'V_410',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_586,(0,5):C.GC_1072,(0,0):C.GC_1243,(0,1):C.GC_991,(0,3):C.GC_1324,(0,4):C.GC_1324})

V_411 = Vertex(name = 'V_411',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_902})

V_412 = Vertex(name = 'V_412',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_587,(0,5):C.GC_1073,(0,0):C.GC_1244,(0,1):C.GC_992,(0,3):C.GC_1325,(0,4):C.GC_1327})

V_413 = Vertex(name = 'V_413',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_904})

V_414 = Vertex(name = 'V_414',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_591,(0,5):C.GC_1077,(0,0):C.GC_1248,(0,1):C.GC_996,(0,3):C.GC_1329,(0,4):C.GC_1331})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_912})

V_416 = Vertex(name = 'V_416',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_589,(0,5):C.GC_1075,(0,0):C.GC_1246,(0,1):C.GC_994,(0,3):C.GC_1327,(0,4):C.GC_1325})

V_417 = Vertex(name = 'V_417',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_908})

V_418 = Vertex(name = 'V_418',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_590,(0,5):C.GC_1076,(0,0):C.GC_1247,(0,1):C.GC_995,(0,3):C.GC_1328,(0,4):C.GC_1328})

V_419 = Vertex(name = 'V_419',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_910})

V_420 = Vertex(name = 'V_420',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_195,(0,2):C.GC_610,(0,0):C.GC_609,(0,1):C.GC_609,(0,4):C.GC_341,(0,5):C.GC_440})

V_421 = Vertex(name = 'V_421',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_306,(0,2):C.GC_612,(0,0):C.GC_611,(0,1):C.GC_611,(0,4):C.GC_342,(0,5):C.GC_441})

V_422 = Vertex(name = 'V_422',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_84,(0,2):C.GC_608,(0,0):C.GC_607,(0,1):C.GC_607,(0,4):C.GC_340,(0,5):C.GC_439})

V_423 = Vertex(name = 'V_423',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_193,(0,2):C.GC_598,(0,0):C.GC_597,(0,1):C.GC_597,(0,4):C.GC_335,(0,5):C.GC_434})

V_424 = Vertex(name = 'V_424',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_304,(0,2):C.GC_600,(0,0):C.GC_599,(0,1):C.GC_599,(0,4):C.GC_336,(0,5):C.GC_435})

V_425 = Vertex(name = 'V_425',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_82,(0,2):C.GC_596,(0,0):C.GC_595,(0,1):C.GC_595,(0,4):C.GC_334,(0,5):C.GC_433})

V_426 = Vertex(name = 'V_426',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_194,(0,2):C.GC_604,(0,0):C.GC_603,(0,1):C.GC_603,(0,4):C.GC_338,(0,5):C.GC_437})

V_427 = Vertex(name = 'V_427',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_305,(0,2):C.GC_606,(0,0):C.GC_605,(0,1):C.GC_605,(0,4):C.GC_339,(0,5):C.GC_438})

V_428 = Vertex(name = 'V_428',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_83,(0,2):C.GC_602,(0,0):C.GC_601,(0,1):C.GC_601,(0,4):C.GC_337,(0,5):C.GC_436})

V_429 = Vertex(name = 'V_429',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_198,(0,2):C.GC_628,(0,0):C.GC_627,(0,1):C.GC_627,(0,4):C.GC_350,(0,5):C.GC_449})

V_430 = Vertex(name = 'V_430',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_309,(0,2):C.GC_630,(0,0):C.GC_629,(0,1):C.GC_629,(0,4):C.GC_351,(0,5):C.GC_450})

V_431 = Vertex(name = 'V_431',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_87,(0,2):C.GC_626,(0,0):C.GC_625,(0,1):C.GC_625,(0,4):C.GC_349,(0,5):C.GC_448})

V_432 = Vertex(name = 'V_432',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_196,(0,2):C.GC_616,(0,0):C.GC_615,(0,1):C.GC_615,(0,4):C.GC_344,(0,5):C.GC_443})

V_433 = Vertex(name = 'V_433',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_307,(0,2):C.GC_618,(0,0):C.GC_617,(0,1):C.GC_617,(0,4):C.GC_345,(0,5):C.GC_444})

V_434 = Vertex(name = 'V_434',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_85,(0,2):C.GC_614,(0,0):C.GC_613,(0,1):C.GC_613,(0,4):C.GC_343,(0,5):C.GC_442})

V_435 = Vertex(name = 'V_435',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_197,(0,2):C.GC_622,(0,0):C.GC_621,(0,1):C.GC_621,(0,4):C.GC_347,(0,5):C.GC_446})

V_436 = Vertex(name = 'V_436',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_308,(0,2):C.GC_624,(0,0):C.GC_623,(0,1):C.GC_623,(0,4):C.GC_348,(0,5):C.GC_447})

V_437 = Vertex(name = 'V_437',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_86,(0,2):C.GC_620,(0,0):C.GC_619,(0,1):C.GC_619,(0,4):C.GC_346,(0,5):C.GC_445})

V_438 = Vertex(name = 'V_438',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_201,(0,2):C.GC_646,(0,0):C.GC_645,(0,1):C.GC_645,(0,4):C.GC_359,(0,5):C.GC_458})

V_439 = Vertex(name = 'V_439',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_312,(0,2):C.GC_648,(0,0):C.GC_647,(0,1):C.GC_647,(0,4):C.GC_360,(0,5):C.GC_459})

V_440 = Vertex(name = 'V_440',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_90,(0,2):C.GC_644,(0,0):C.GC_643,(0,1):C.GC_643,(0,4):C.GC_358,(0,5):C.GC_457})

V_441 = Vertex(name = 'V_441',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_199,(0,2):C.GC_634,(0,0):C.GC_633,(0,1):C.GC_633,(0,4):C.GC_353,(0,5):C.GC_452})

V_442 = Vertex(name = 'V_442',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_310,(0,2):C.GC_636,(0,0):C.GC_635,(0,1):C.GC_635,(0,4):C.GC_354,(0,5):C.GC_453})

V_443 = Vertex(name = 'V_443',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_88,(0,2):C.GC_632,(0,0):C.GC_631,(0,1):C.GC_631,(0,4):C.GC_352,(0,5):C.GC_451})

V_444 = Vertex(name = 'V_444',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_200,(0,2):C.GC_640,(0,0):C.GC_639,(0,1):C.GC_639,(0,4):C.GC_356,(0,5):C.GC_455})

V_445 = Vertex(name = 'V_445',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_311,(0,0):C.GC_641,(0,1):C.GC_641,(0,2):C.GC_642,(0,4):C.GC_357,(0,5):C.GC_456})

V_446 = Vertex(name = 'V_446',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_89,(0,2):C.GC_638,(0,0):C.GC_637,(0,1):C.GC_637,(0,4):C.GC_355,(0,5):C.GC_454})

V_447 = Vertex(name = 'V_447',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_204,(0,2):C.GC_664,(0,0):C.GC_663,(0,1):C.GC_663,(0,4):C.GC_368,(0,5):C.GC_467})

V_448 = Vertex(name = 'V_448',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_315,(0,2):C.GC_666,(0,0):C.GC_665,(0,1):C.GC_665,(0,4):C.GC_369,(0,5):C.GC_468})

V_449 = Vertex(name = 'V_449',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_93,(0,2):C.GC_662,(0,0):C.GC_661,(0,1):C.GC_661,(0,4):C.GC_367,(0,5):C.GC_466})

V_450 = Vertex(name = 'V_450',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_202,(0,2):C.GC_652,(0,0):C.GC_651,(0,1):C.GC_651,(0,4):C.GC_362,(0,5):C.GC_461})

V_451 = Vertex(name = 'V_451',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_313,(0,2):C.GC_654,(0,0):C.GC_653,(0,1):C.GC_653,(0,4):C.GC_363,(0,5):C.GC_462})

V_452 = Vertex(name = 'V_452',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_91,(0,2):C.GC_650,(0,0):C.GC_649,(0,1):C.GC_649,(0,4):C.GC_361,(0,5):C.GC_460})

V_453 = Vertex(name = 'V_453',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_203,(0,2):C.GC_658,(0,0):C.GC_657,(0,1):C.GC_657,(0,4):C.GC_365,(0,5):C.GC_464})

V_454 = Vertex(name = 'V_454',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_314,(0,2):C.GC_660,(0,0):C.GC_659,(0,1):C.GC_659,(0,4):C.GC_366,(0,5):C.GC_465})

V_455 = Vertex(name = 'V_455',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_92,(0,2):C.GC_656,(0,0):C.GC_655,(0,1):C.GC_655,(0,4):C.GC_364,(0,5):C.GC_463})

V_456 = Vertex(name = 'V_456',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_207,(0,2):C.GC_682,(0,0):C.GC_681,(0,1):C.GC_681,(0,4):C.GC_377,(0,5):C.GC_476})

V_457 = Vertex(name = 'V_457',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_318,(0,2):C.GC_684,(0,0):C.GC_683,(0,1):C.GC_683,(0,4):C.GC_378,(0,5):C.GC_477})

V_458 = Vertex(name = 'V_458',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_96,(0,2):C.GC_680,(0,0):C.GC_679,(0,1):C.GC_679,(0,4):C.GC_376,(0,5):C.GC_475})

V_459 = Vertex(name = 'V_459',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_205,(0,2):C.GC_670,(0,0):C.GC_669,(0,1):C.GC_669,(0,4):C.GC_371,(0,5):C.GC_470})

V_460 = Vertex(name = 'V_460',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_316,(0,2):C.GC_672,(0,0):C.GC_671,(0,1):C.GC_671,(0,4):C.GC_372,(0,5):C.GC_471})

V_461 = Vertex(name = 'V_461',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_94,(0,2):C.GC_668,(0,0):C.GC_667,(0,1):C.GC_667,(0,4):C.GC_370,(0,5):C.GC_469})

V_462 = Vertex(name = 'V_462',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_206,(0,2):C.GC_676,(0,0):C.GC_675,(0,1):C.GC_675,(0,4):C.GC_374,(0,5):C.GC_473})

V_463 = Vertex(name = 'V_463',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_317,(0,2):C.GC_678,(0,0):C.GC_677,(0,1):C.GC_677,(0,4):C.GC_375,(0,5):C.GC_474})

V_464 = Vertex(name = 'V_464',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_95,(0,2):C.GC_674,(0,0):C.GC_673,(0,1):C.GC_673,(0,4):C.GC_373,(0,5):C.GC_472})

V_465 = Vertex(name = 'V_465',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_210,(0,2):C.GC_700,(0,0):C.GC_699,(0,1):C.GC_699,(0,4):C.GC_386,(0,5):C.GC_485})

V_466 = Vertex(name = 'V_466',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_321,(0,2):C.GC_702,(0,0):C.GC_701,(0,1):C.GC_701,(0,4):C.GC_387,(0,5):C.GC_486})

V_467 = Vertex(name = 'V_467',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_99,(0,2):C.GC_698,(0,0):C.GC_697,(0,1):C.GC_697,(0,4):C.GC_385,(0,5):C.GC_484})

V_468 = Vertex(name = 'V_468',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_208,(0,2):C.GC_688,(0,0):C.GC_687,(0,1):C.GC_687,(0,4):C.GC_380,(0,5):C.GC_479})

V_469 = Vertex(name = 'V_469',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_319,(0,2):C.GC_690,(0,0):C.GC_689,(0,1):C.GC_689,(0,4):C.GC_381,(0,5):C.GC_480})

V_470 = Vertex(name = 'V_470',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_97,(0,2):C.GC_686,(0,0):C.GC_685,(0,1):C.GC_685,(0,4):C.GC_379,(0,5):C.GC_478})

V_471 = Vertex(name = 'V_471',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_209,(0,2):C.GC_694,(0,0):C.GC_693,(0,1):C.GC_693,(0,4):C.GC_383,(0,5):C.GC_482})

V_472 = Vertex(name = 'V_472',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_320,(0,2):C.GC_696,(0,0):C.GC_695,(0,1):C.GC_695,(0,4):C.GC_384,(0,5):C.GC_483})

V_473 = Vertex(name = 'V_473',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_98,(0,2):C.GC_692,(0,0):C.GC_691,(0,1):C.GC_691,(0,4):C.GC_382,(0,5):C.GC_481})

V_474 = Vertex(name = 'V_474',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_213,(0,2):C.GC_718,(0,0):C.GC_717,(0,1):C.GC_717,(0,4):C.GC_395,(0,5):C.GC_494})

V_475 = Vertex(name = 'V_475',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_324,(0,2):C.GC_720,(0,0):C.GC_719,(0,1):C.GC_719,(0,4):C.GC_396,(0,5):C.GC_495})

V_476 = Vertex(name = 'V_476',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_102,(0,2):C.GC_716,(0,0):C.GC_715,(0,1):C.GC_715,(0,4):C.GC_394,(0,5):C.GC_493})

V_477 = Vertex(name = 'V_477',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_211,(0,2):C.GC_706,(0,0):C.GC_705,(0,1):C.GC_705,(0,4):C.GC_389,(0,5):C.GC_488})

V_478 = Vertex(name = 'V_478',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_322,(0,2):C.GC_708,(0,0):C.GC_707,(0,1):C.GC_707,(0,4):C.GC_390,(0,5):C.GC_489})

V_479 = Vertex(name = 'V_479',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_100,(0,2):C.GC_704,(0,0):C.GC_703,(0,1):C.GC_703,(0,4):C.GC_388,(0,5):C.GC_487})

V_480 = Vertex(name = 'V_480',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_212,(0,2):C.GC_712,(0,0):C.GC_711,(0,1):C.GC_711,(0,4):C.GC_392,(0,5):C.GC_491})

V_481 = Vertex(name = 'V_481',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_323,(0,2):C.GC_714,(0,0):C.GC_713,(0,1):C.GC_713,(0,4):C.GC_393,(0,5):C.GC_492})

V_482 = Vertex(name = 'V_482',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_101,(0,2):C.GC_710,(0,0):C.GC_709,(0,1):C.GC_709,(0,4):C.GC_391,(0,5):C.GC_490})

V_483 = Vertex(name = 'V_483',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_216,(0,2):C.GC_736,(0,0):C.GC_735,(0,1):C.GC_735,(0,4):C.GC_404,(0,5):C.GC_503})

V_484 = Vertex(name = 'V_484',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_327,(0,2):C.GC_738,(0,0):C.GC_737,(0,1):C.GC_737,(0,4):C.GC_405,(0,5):C.GC_504})

V_485 = Vertex(name = 'V_485',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_105,(0,2):C.GC_734,(0,0):C.GC_733,(0,1):C.GC_733,(0,4):C.GC_403,(0,5):C.GC_502})

V_486 = Vertex(name = 'V_486',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_214,(0,2):C.GC_724,(0,0):C.GC_723,(0,1):C.GC_723,(0,4):C.GC_398,(0,5):C.GC_497})

V_487 = Vertex(name = 'V_487',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_325,(0,2):C.GC_726,(0,0):C.GC_725,(0,1):C.GC_725,(0,4):C.GC_399,(0,5):C.GC_498})

V_488 = Vertex(name = 'V_488',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_103,(0,2):C.GC_722,(0,0):C.GC_721,(0,1):C.GC_721,(0,4):C.GC_397,(0,5):C.GC_496})

V_489 = Vertex(name = 'V_489',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_215,(0,2):C.GC_730,(0,0):C.GC_729,(0,1):C.GC_729,(0,4):C.GC_401,(0,5):C.GC_500})

V_490 = Vertex(name = 'V_490',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_326,(0,2):C.GC_732,(0,0):C.GC_731,(0,1):C.GC_731,(0,4):C.GC_402,(0,5):C.GC_501})

V_491 = Vertex(name = 'V_491',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_104,(0,2):C.GC_728,(0,0):C.GC_727,(0,1):C.GC_727,(0,4):C.GC_400,(0,5):C.GC_499})

V_492 = Vertex(name = 'V_492',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_219,(0,2):C.GC_754,(0,0):C.GC_753,(0,1):C.GC_753,(0,4):C.GC_413,(0,5):C.GC_512})

V_493 = Vertex(name = 'V_493',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_330,(0,2):C.GC_756,(0,0):C.GC_755,(0,1):C.GC_755,(0,4):C.GC_414,(0,5):C.GC_513})

V_494 = Vertex(name = 'V_494',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_108,(0,2):C.GC_752,(0,0):C.GC_751,(0,1):C.GC_751,(0,4):C.GC_412,(0,5):C.GC_511})

V_495 = Vertex(name = 'V_495',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_217,(0,2):C.GC_742,(0,0):C.GC_741,(0,1):C.GC_741,(0,4):C.GC_407,(0,5):C.GC_506})

V_496 = Vertex(name = 'V_496',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_328,(0,2):C.GC_744,(0,0):C.GC_743,(0,1):C.GC_743,(0,4):C.GC_408,(0,5):C.GC_507})

V_497 = Vertex(name = 'V_497',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_106,(0,2):C.GC_740,(0,0):C.GC_739,(0,1):C.GC_739,(0,4):C.GC_406,(0,5):C.GC_505})

V_498 = Vertex(name = 'V_498',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_218,(0,2):C.GC_748,(0,0):C.GC_747,(0,1):C.GC_747,(0,4):C.GC_410,(0,5):C.GC_509})

V_499 = Vertex(name = 'V_499',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_329,(0,2):C.GC_750,(0,0):C.GC_749,(0,1):C.GC_749,(0,4):C.GC_411,(0,5):C.GC_510})

V_500 = Vertex(name = 'V_500',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_107,(0,2):C.GC_746,(0,0):C.GC_745,(0,1):C.GC_745,(0,4):C.GC_409,(0,5):C.GC_508})

V_501 = Vertex(name = 'V_501',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_1461})

V_502 = Vertex(name = 'V_502',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_1468})

V_503 = Vertex(name = 'V_503',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_1634})

V_504 = Vertex(name = 'V_504',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_1463})

V_505 = Vertex(name = 'V_505',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_1483})

V_506 = Vertex(name = 'V_506',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_1469})

V_507 = Vertex(name = 'V_507',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_1484})

V_508 = Vertex(name = 'V_508',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_1542})

V_509 = Vertex(name = 'V_509',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_1914})

V_510 = Vertex(name = 'V_510',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_1470})

V_511 = Vertex(name = 'V_511',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV6 ],
               couplings = {(0,1):C.GC_1462,(0,0):C.GC_1579})

V_512 = Vertex(name = 'V_512',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_1734})

V_513 = Vertex(name = 'V_513',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV6 ],
               couplings = {(0,1):C.GC_1462,(0,0):C.GC_1583})

V_514 = Vertex(name = 'V_514',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_1738})

V_515 = Vertex(name = 'V_515',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV6 ],
               couplings = {(0,1):C.GC_1462,(0,0):C.GC_1587})

V_516 = Vertex(name = 'V_516',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_1742})

V_517 = Vertex(name = 'V_517',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6, L.FFV9 ],
               couplings = {(0,1):C.GC_1460,(0,0):C.GC_1774,(0,2):C.GC_2576})

V_518 = Vertex(name = 'V_518',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1837,(0,1):C.GC_2597})

V_519 = Vertex(name = 'V_519',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6, L.FFV9 ],
               couplings = {(0,1):C.GC_1460,(0,0):C.GC_1778,(0,2):C.GC_2878})

V_520 = Vertex(name = 'V_520',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1841,(0,1):C.GC_2899})

V_521 = Vertex(name = 'V_521',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6, L.FFV9 ],
               couplings = {(0,1):C.GC_1460,(0,0):C.GC_1770,(0,2):C.GC_2274})

V_522 = Vertex(name = 'V_522',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1833,(0,1):C.GC_2295})

V_523 = Vertex(name = 'V_523',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV6 ],
               couplings = {(0,1):C.GC_1459,(0,0):C.GC_1569})

V_524 = Vertex(name = 'V_524',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_1724})

V_525 = Vertex(name = 'V_525',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV6 ],
               couplings = {(0,1):C.GC_1459,(0,0):C.GC_1561})

V_526 = Vertex(name = 'V_526',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_1716})

V_527 = Vertex(name = 'V_527',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV6 ],
               couplings = {(0,1):C.GC_1459,(0,0):C.GC_1565})

V_528 = Vertex(name = 'V_528',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_1720})

V_529 = Vertex(name = 'V_529',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1464})

V_530 = Vertex(name = 'V_530',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1464})

V_531 = Vertex(name = 'V_531',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1464})

V_532 = Vertex(name = 'V_532',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1464})

V_533 = Vertex(name = 'V_533',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1464})

V_534 = Vertex(name = 'V_534',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1464})

V_535 = Vertex(name = 'V_535',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1559,(0,3):C.GC_2574,(0,0):C.GC_1477,(0,2):C.GC_1757})

V_536 = Vertex(name = 'V_536',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2607})

V_537 = Vertex(name = 'V_537',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1553,(0,3):C.GC_2572,(0,0):C.GC_1475,(0,2):C.GC_1755})

V_538 = Vertex(name = 'V_538',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2605})

V_539 = Vertex(name = 'V_539',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1556,(0,3):C.GC_2573,(0,0):C.GC_1476,(0,2):C.GC_1756})

V_540 = Vertex(name = 'V_540',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2606})

V_541 = Vertex(name = 'V_541',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1560,(0,3):C.GC_2875,(0,0):C.GC_1480,(0,2):C.GC_1760})

V_542 = Vertex(name = 'V_542',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2908})

V_543 = Vertex(name = 'V_543',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1554,(0,3):C.GC_2873,(0,0):C.GC_1478,(0,2):C.GC_1758})

V_544 = Vertex(name = 'V_544',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2906})

V_545 = Vertex(name = 'V_545',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1557,(0,3):C.GC_2874,(0,0):C.GC_1479,(0,2):C.GC_1759})

V_546 = Vertex(name = 'V_546',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2907})

V_547 = Vertex(name = 'V_547',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1558,(0,3):C.GC_2273,(0,0):C.GC_1474,(0,2):C.GC_1754})

V_548 = Vertex(name = 'V_548',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2306})

V_549 = Vertex(name = 'V_549',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1552,(0,3):C.GC_2271,(0,0):C.GC_1472,(0,2):C.GC_1752})

V_550 = Vertex(name = 'V_550',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2304})

V_551 = Vertex(name = 'V_551',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1555,(0,3):C.GC_2272,(0,0):C.GC_1473,(0,2):C.GC_1753})

V_552 = Vertex(name = 'V_552',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2305})

V_553 = Vertex(name = 'V_553',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1766,(0,3):C.GC_1559,(0,0):C.GC_1920,(0,2):C.GC_1757})

V_554 = Vertex(name = 'V_554',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2011})

V_555 = Vertex(name = 'V_555',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1769,(0,3):C.GC_1560,(0,0):C.GC_1923,(0,2):C.GC_1760})

V_556 = Vertex(name = 'V_556',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2614})

V_557 = Vertex(name = 'V_557',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1763,(0,3):C.GC_1558,(0,0):C.GC_1917,(0,2):C.GC_1754})

V_558 = Vertex(name = 'V_558',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2007})

V_559 = Vertex(name = 'V_559',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1764,(0,3):C.GC_1553,(0,0):C.GC_1918,(0,2):C.GC_1755})

V_560 = Vertex(name = 'V_560',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2008})

V_561 = Vertex(name = 'V_561',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1767,(0,3):C.GC_1554,(0,0):C.GC_1921,(0,2):C.GC_1758})

V_562 = Vertex(name = 'V_562',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2012})

V_563 = Vertex(name = 'V_563',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1761,(0,3):C.GC_1552,(0,0):C.GC_1915,(0,2):C.GC_1752})

V_564 = Vertex(name = 'V_564',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2005})

V_565 = Vertex(name = 'V_565',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1765,(0,3):C.GC_1556,(0,0):C.GC_1919,(0,2):C.GC_1756})

V_566 = Vertex(name = 'V_566',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2009})

V_567 = Vertex(name = 'V_567',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1768,(0,3):C.GC_1557,(0,0):C.GC_1922,(0,2):C.GC_1759})

V_568 = Vertex(name = 'V_568',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2314})

V_569 = Vertex(name = 'V_569',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1762,(0,3):C.GC_1555,(0,0):C.GC_1916,(0,2):C.GC_1753})

V_570 = Vertex(name = 'V_570',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2006})

V_571 = Vertex(name = 'V_571',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,1):C.GC_1543,(0,0):C.GC_1471})

V_572 = Vertex(name = 'V_572',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1743})

V_573 = Vertex(name = 'V_573',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,1):C.GC_1547,(0,0):C.GC_1471})

V_574 = Vertex(name = 'V_574',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1747})

V_575 = Vertex(name = 'V_575',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,1):C.GC_1551,(0,0):C.GC_1471})

V_576 = Vertex(name = 'V_576',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1751})

V_577 = Vertex(name = 'V_577',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1543,(0,0):C.GC_1471})

V_578 = Vertex(name = 'V_578',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1743})

V_579 = Vertex(name = 'V_579',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1547,(0,0):C.GC_1471})

V_580 = Vertex(name = 'V_580',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1747})

V_581 = Vertex(name = 'V_581',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1551,(0,0):C.GC_1471})

V_582 = Vertex(name = 'V_582',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1751})

V_583 = Vertex(name = 'V_583',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_1481,(0,3):C.GC_1521,(0,2):C.GC_1991,(0,1):C.GC_1783,(0,4):C.GC_2579})

V_584 = Vertex(name = 'V_584',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2610,(0,1):C.GC_1828,(0,2):C.GC_2594})

V_585 = Vertex(name = 'V_585',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2611})

V_586 = Vertex(name = 'V_586',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_1481,(0,3):C.GC_1521,(0,2):C.GC_1995,(0,1):C.GC_1787,(0,4):C.GC_2881})

V_587 = Vertex(name = 'V_587',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2913,(0,1):C.GC_1832,(0,2):C.GC_2896})

V_588 = Vertex(name = 'V_588',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2914})

V_589 = Vertex(name = 'V_589',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_1481,(0,3):C.GC_1521,(0,2):C.GC_1987,(0,1):C.GC_1779,(0,4):C.GC_2277})

V_590 = Vertex(name = 'V_590',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2307,(0,1):C.GC_1824,(0,2):C.GC_2292})

V_591 = Vertex(name = 'V_591',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2308})

V_592 = Vertex(name = 'V_592',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1482,(0,3):C.GC_1521,(0,2):C.GC_1977,(0,0):C.GC_1578})

V_593 = Vertex(name = 'V_593',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2 ],
               couplings = {(0,1):C.GC_1941,(0,0):C.GC_1715})

V_594 = Vertex(name = 'V_594',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1968})

V_595 = Vertex(name = 'V_595',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1482,(0,3):C.GC_1521,(0,2):C.GC_1969,(0,0):C.GC_1570})

V_596 = Vertex(name = 'V_596',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2 ],
               couplings = {(0,1):C.GC_1933,(0,0):C.GC_1707})

V_597 = Vertex(name = 'V_597',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1960})

V_598 = Vertex(name = 'V_598',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV4, L.FFV5 ],
               couplings = {(0,1):C.GC_1482,(0,3):C.GC_1521,(0,2):C.GC_1973,(0,0):C.GC_1574})

V_599 = Vertex(name = 'V_599',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2 ],
               couplings = {(0,1):C.GC_1937,(0,0):C.GC_1711})

V_600 = Vertex(name = 'V_600',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1964})

V_601 = Vertex(name = 'V_601',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1541})

V_602 = Vertex(name = 'V_602',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1924})

V_603 = Vertex(name = 'V_603',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1942})

V_604 = Vertex(name = 'V_604',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1541})

V_605 = Vertex(name = 'V_605',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1928})

V_606 = Vertex(name = 'V_606',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1950})

V_607 = Vertex(name = 'V_607',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1541})

V_608 = Vertex(name = 'V_608',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1932})

V_609 = Vertex(name = 'V_609',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1958})

V_610 = Vertex(name = 'V_610',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV4, L.FFV7 ],
               couplings = {(0,1):C.GC_1482,(0,3):C.GC_1522,(0,2):C.GC_1978,(0,0):C.GC_1588})

V_611 = Vertex(name = 'V_611',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV2 ],
               couplings = {(0,1):C.GC_1924,(0,0):C.GC_1725})

V_612 = Vertex(name = 'V_612',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1943})

V_613 = Vertex(name = 'V_613',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV4, L.FFV7 ],
               couplings = {(0,1):C.GC_1482,(0,3):C.GC_1522,(0,2):C.GC_1982,(0,0):C.GC_1592})

V_614 = Vertex(name = 'V_614',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV2 ],
               couplings = {(0,1):C.GC_1928,(0,0):C.GC_1729})

V_615 = Vertex(name = 'V_615',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1951})

V_616 = Vertex(name = 'V_616',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV4, L.FFV7 ],
               couplings = {(0,1):C.GC_1482,(0,3):C.GC_1522,(0,2):C.GC_1986,(0,0):C.GC_1596})

V_617 = Vertex(name = 'V_617',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV2 ],
               couplings = {(0,1):C.GC_1932,(0,0):C.GC_1733})

V_618 = Vertex(name = 'V_618',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1959})

V_619 = Vertex(name = 'V_619',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2461,(0,1):C.GC_1337})

V_620 = Vertex(name = 'V_620',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2471})

V_621 = Vertex(name = 'V_621',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2497,(0,1):C.GC_1338})

V_622 = Vertex(name = 'V_622',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2507})

V_623 = Vertex(name = 'V_623',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2425,(0,1):C.GC_1336})

V_624 = Vertex(name = 'V_624',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2435})

V_625 = Vertex(name = 'V_625',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2762,(0,1):C.GC_1340})

V_626 = Vertex(name = 'V_626',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2772})

V_627 = Vertex(name = 'V_627',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2798,(0,1):C.GC_1341})

V_628 = Vertex(name = 'V_628',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2808})

V_629 = Vertex(name = 'V_629',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2726,(0,1):C.GC_1339})

V_630 = Vertex(name = 'V_630',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2736})

V_631 = Vertex(name = 'V_631',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2160,(0,1):C.GC_1334})

V_632 = Vertex(name = 'V_632',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2170})

V_633 = Vertex(name = 'V_633',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2196,(0,1):C.GC_1335})

V_634 = Vertex(name = 'V_634',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2206})

V_635 = Vertex(name = 'V_635',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2124,(0,1):C.GC_1333})

V_636 = Vertex(name = 'V_636',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2134})

V_637 = Vertex(name = 'V_637',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2462,(0,1):C.GC_1346})

V_638 = Vertex(name = 'V_638',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2473})

V_639 = Vertex(name = 'V_639',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2498,(0,1):C.GC_1347})

V_640 = Vertex(name = 'V_640',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2509})

V_641 = Vertex(name = 'V_641',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2426,(0,1):C.GC_1345})

V_642 = Vertex(name = 'V_642',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2437})

V_643 = Vertex(name = 'V_643',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2763,(0,1):C.GC_1349})

V_644 = Vertex(name = 'V_644',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2774})

V_645 = Vertex(name = 'V_645',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2799,(0,1):C.GC_1350})

V_646 = Vertex(name = 'V_646',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2810})

V_647 = Vertex(name = 'V_647',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2727,(0,1):C.GC_1348})

V_648 = Vertex(name = 'V_648',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2738})

V_649 = Vertex(name = 'V_649',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2161,(0,1):C.GC_1343})

V_650 = Vertex(name = 'V_650',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2172})

V_651 = Vertex(name = 'V_651',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2197,(0,1):C.GC_1344})

V_652 = Vertex(name = 'V_652',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2208})

V_653 = Vertex(name = 'V_653',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2125,(0,1):C.GC_1342})

V_654 = Vertex(name = 'V_654',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2136})

V_655 = Vertex(name = 'V_655',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2463,(0,1):C.GC_1355})

V_656 = Vertex(name = 'V_656',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2475})

V_657 = Vertex(name = 'V_657',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2499,(0,1):C.GC_1356})

V_658 = Vertex(name = 'V_658',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2511})

V_659 = Vertex(name = 'V_659',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2427,(0,1):C.GC_1354})

V_660 = Vertex(name = 'V_660',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2439})

V_661 = Vertex(name = 'V_661',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2764,(0,1):C.GC_1358})

V_662 = Vertex(name = 'V_662',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2776})

V_663 = Vertex(name = 'V_663',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2800,(0,1):C.GC_1359})

V_664 = Vertex(name = 'V_664',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2812})

V_665 = Vertex(name = 'V_665',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2728,(0,1):C.GC_1357})

V_666 = Vertex(name = 'V_666',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2740})

V_667 = Vertex(name = 'V_667',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2162,(0,1):C.GC_1352})

V_668 = Vertex(name = 'V_668',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2174})

V_669 = Vertex(name = 'V_669',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2198,(0,1):C.GC_1353})

V_670 = Vertex(name = 'V_670',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2210})

V_671 = Vertex(name = 'V_671',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2126,(0,1):C.GC_1351})

V_672 = Vertex(name = 'V_672',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2138})

V_673 = Vertex(name = 'V_673',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2464,(0,1):C.GC_1364})

V_674 = Vertex(name = 'V_674',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2477})

V_675 = Vertex(name = 'V_675',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2500,(0,1):C.GC_1365})

V_676 = Vertex(name = 'V_676',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2513})

V_677 = Vertex(name = 'V_677',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2428,(0,1):C.GC_1363})

V_678 = Vertex(name = 'V_678',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2441})

V_679 = Vertex(name = 'V_679',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2765,(0,1):C.GC_1367})

V_680 = Vertex(name = 'V_680',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2778})

V_681 = Vertex(name = 'V_681',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2801,(0,1):C.GC_1368})

V_682 = Vertex(name = 'V_682',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2814})

V_683 = Vertex(name = 'V_683',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2729,(0,1):C.GC_1366})

V_684 = Vertex(name = 'V_684',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2742})

V_685 = Vertex(name = 'V_685',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2163,(0,1):C.GC_1361})

V_686 = Vertex(name = 'V_686',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2176})

V_687 = Vertex(name = 'V_687',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2199,(0,1):C.GC_1362})

V_688 = Vertex(name = 'V_688',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2212})

V_689 = Vertex(name = 'V_689',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2127,(0,1):C.GC_1360})

V_690 = Vertex(name = 'V_690',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2140})

V_691 = Vertex(name = 'V_691',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2465,(0,1):C.GC_1373})

V_692 = Vertex(name = 'V_692',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2479})

V_693 = Vertex(name = 'V_693',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2501,(0,1):C.GC_1374})

V_694 = Vertex(name = 'V_694',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2515})

V_695 = Vertex(name = 'V_695',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2429,(0,1):C.GC_1372})

V_696 = Vertex(name = 'V_696',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2443})

V_697 = Vertex(name = 'V_697',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2766,(0,1):C.GC_1376})

V_698 = Vertex(name = 'V_698',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2780})

V_699 = Vertex(name = 'V_699',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2802,(0,1):C.GC_1377})

V_700 = Vertex(name = 'V_700',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2816})

V_701 = Vertex(name = 'V_701',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2730,(0,1):C.GC_1375})

V_702 = Vertex(name = 'V_702',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2744})

V_703 = Vertex(name = 'V_703',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2164,(0,1):C.GC_1370})

V_704 = Vertex(name = 'V_704',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2178})

V_705 = Vertex(name = 'V_705',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2200,(0,1):C.GC_1371})

V_706 = Vertex(name = 'V_706',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2214})

V_707 = Vertex(name = 'V_707',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2128,(0,1):C.GC_1369})

V_708 = Vertex(name = 'V_708',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2142})

V_709 = Vertex(name = 'V_709',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2466,(0,1):C.GC_1382})

V_710 = Vertex(name = 'V_710',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2481})

V_711 = Vertex(name = 'V_711',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2502,(0,1):C.GC_1383})

V_712 = Vertex(name = 'V_712',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2517})

V_713 = Vertex(name = 'V_713',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2430,(0,1):C.GC_1381})

V_714 = Vertex(name = 'V_714',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2445})

V_715 = Vertex(name = 'V_715',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2767,(0,1):C.GC_1385})

V_716 = Vertex(name = 'V_716',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2782})

V_717 = Vertex(name = 'V_717',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2803,(0,1):C.GC_1386})

V_718 = Vertex(name = 'V_718',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2818})

V_719 = Vertex(name = 'V_719',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2731,(0,1):C.GC_1384})

V_720 = Vertex(name = 'V_720',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2746})

V_721 = Vertex(name = 'V_721',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2165,(0,1):C.GC_1379})

V_722 = Vertex(name = 'V_722',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2180})

V_723 = Vertex(name = 'V_723',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2201,(0,1):C.GC_1380})

V_724 = Vertex(name = 'V_724',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2216})

V_725 = Vertex(name = 'V_725',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2129,(0,1):C.GC_1378})

V_726 = Vertex(name = 'V_726',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2144})

V_727 = Vertex(name = 'V_727',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2467,(0,1):C.GC_1391})

V_728 = Vertex(name = 'V_728',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2483})

V_729 = Vertex(name = 'V_729',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2503,(0,1):C.GC_1392})

V_730 = Vertex(name = 'V_730',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2519})

V_731 = Vertex(name = 'V_731',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2431,(0,1):C.GC_1390})

V_732 = Vertex(name = 'V_732',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2447})

V_733 = Vertex(name = 'V_733',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2768,(0,1):C.GC_1394})

V_734 = Vertex(name = 'V_734',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2784})

V_735 = Vertex(name = 'V_735',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2804,(0,1):C.GC_1395})

V_736 = Vertex(name = 'V_736',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2820})

V_737 = Vertex(name = 'V_737',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2732,(0,1):C.GC_1393})

V_738 = Vertex(name = 'V_738',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2748})

V_739 = Vertex(name = 'V_739',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2166,(0,1):C.GC_1388})

V_740 = Vertex(name = 'V_740',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2182})

V_741 = Vertex(name = 'V_741',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2202,(0,1):C.GC_1389})

V_742 = Vertex(name = 'V_742',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2218})

V_743 = Vertex(name = 'V_743',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2130,(0,1):C.GC_1387})

V_744 = Vertex(name = 'V_744',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2146})

V_745 = Vertex(name = 'V_745',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2468,(0,1):C.GC_1400})

V_746 = Vertex(name = 'V_746',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2485})

V_747 = Vertex(name = 'V_747',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2504,(0,1):C.GC_1401})

V_748 = Vertex(name = 'V_748',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2521})

V_749 = Vertex(name = 'V_749',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2432,(0,1):C.GC_1399})

V_750 = Vertex(name = 'V_750',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2449})

V_751 = Vertex(name = 'V_751',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2769,(0,1):C.GC_1403})

V_752 = Vertex(name = 'V_752',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2786})

V_753 = Vertex(name = 'V_753',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2805,(0,1):C.GC_1404})

V_754 = Vertex(name = 'V_754',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2822})

V_755 = Vertex(name = 'V_755',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2733,(0,1):C.GC_1402})

V_756 = Vertex(name = 'V_756',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2750})

V_757 = Vertex(name = 'V_757',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2167,(0,1):C.GC_1397})

V_758 = Vertex(name = 'V_758',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2184})

V_759 = Vertex(name = 'V_759',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2203,(0,1):C.GC_1398})

V_760 = Vertex(name = 'V_760',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2220})

V_761 = Vertex(name = 'V_761',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2131,(0,1):C.GC_1396})

V_762 = Vertex(name = 'V_762',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2148})

V_763 = Vertex(name = 'V_763',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2469,(0,1):C.GC_1409})

V_764 = Vertex(name = 'V_764',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2487})

V_765 = Vertex(name = 'V_765',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2505,(0,1):C.GC_1410})

V_766 = Vertex(name = 'V_766',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2523})

V_767 = Vertex(name = 'V_767',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2433,(0,1):C.GC_1408})

V_768 = Vertex(name = 'V_768',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2451})

V_769 = Vertex(name = 'V_769',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2770,(0,1):C.GC_1412})

V_770 = Vertex(name = 'V_770',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2788})

V_771 = Vertex(name = 'V_771',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2806,(0,1):C.GC_1413})

V_772 = Vertex(name = 'V_772',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2824})

V_773 = Vertex(name = 'V_773',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2734,(0,1):C.GC_1411})

V_774 = Vertex(name = 'V_774',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2752})

V_775 = Vertex(name = 'V_775',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2168,(0,1):C.GC_1406})

V_776 = Vertex(name = 'V_776',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2186})

V_777 = Vertex(name = 'V_777',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2204,(0,1):C.GC_1407})

V_778 = Vertex(name = 'V_778',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2222})

V_779 = Vertex(name = 'V_779',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2132,(0,1):C.GC_1405})

V_780 = Vertex(name = 'V_780',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_2150})

V_781 = Vertex(name = 'V_781',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_1179})

V_782 = Vertex(name = 'V_782',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_773})

V_783 = Vertex(name = 'V_783',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_520,(0,1):C.GC_1177})

V_784 = Vertex(name = 'V_784',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_769})

V_785 = Vertex(name = 'V_785',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_521,(0,1):C.GC_1178})

V_786 = Vertex(name = 'V_786',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_771})

V_787 = Vertex(name = 'V_787',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_516,(0,1):C.GC_1173})

V_788 = Vertex(name = 'V_788',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_761})

V_789 = Vertex(name = 'V_789',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_1171})

V_790 = Vertex(name = 'V_790',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_757})

V_791 = Vertex(name = 'V_791',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_515,(0,1):C.GC_1172})

V_792 = Vertex(name = 'V_792',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_759})

V_793 = Vertex(name = 'V_793',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_1176})

V_794 = Vertex(name = 'V_794',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_767})

V_795 = Vertex(name = 'V_795',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_517,(0,1):C.GC_1174})

V_796 = Vertex(name = 'V_796',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_763})

V_797 = Vertex(name = 'V_797',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_518,(0,1):C.GC_1175})

V_798 = Vertex(name = 'V_798',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_765})

V_799 = Vertex(name = 'V_799',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_1188})

V_800 = Vertex(name = 'V_800',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_791})

V_801 = Vertex(name = 'V_801',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_529,(0,1):C.GC_1186})

V_802 = Vertex(name = 'V_802',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_787})

V_803 = Vertex(name = 'V_803',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_530,(0,1):C.GC_1187})

V_804 = Vertex(name = 'V_804',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_789})

V_805 = Vertex(name = 'V_805',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_525,(0,1):C.GC_1182})

V_806 = Vertex(name = 'V_806',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_779})

V_807 = Vertex(name = 'V_807',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_523,(0,1):C.GC_1180})

V_808 = Vertex(name = 'V_808',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_775})

V_809 = Vertex(name = 'V_809',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_524,(0,1):C.GC_1181})

V_810 = Vertex(name = 'V_810',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_777})

V_811 = Vertex(name = 'V_811',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_528,(0,1):C.GC_1185})

V_812 = Vertex(name = 'V_812',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_785})

V_813 = Vertex(name = 'V_813',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_526,(0,1):C.GC_1183})

V_814 = Vertex(name = 'V_814',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_781})

V_815 = Vertex(name = 'V_815',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_527,(0,1):C.GC_1184})

V_816 = Vertex(name = 'V_816',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_783})

V_817 = Vertex(name = 'V_817',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_540,(0,1):C.GC_1197})

V_818 = Vertex(name = 'V_818',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_809})

V_819 = Vertex(name = 'V_819',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_538,(0,1):C.GC_1195})

V_820 = Vertex(name = 'V_820',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_805})

V_821 = Vertex(name = 'V_821',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_539,(0,1):C.GC_1196})

V_822 = Vertex(name = 'V_822',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_807})

V_823 = Vertex(name = 'V_823',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_534,(0,1):C.GC_1191})

V_824 = Vertex(name = 'V_824',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_797})

V_825 = Vertex(name = 'V_825',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_532,(0,1):C.GC_1189})

V_826 = Vertex(name = 'V_826',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_793})

V_827 = Vertex(name = 'V_827',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_533,(0,1):C.GC_1190})

V_828 = Vertex(name = 'V_828',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_795})

V_829 = Vertex(name = 'V_829',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_537,(0,1):C.GC_1194})

V_830 = Vertex(name = 'V_830',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_803})

V_831 = Vertex(name = 'V_831',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_535,(0,1):C.GC_1192})

V_832 = Vertex(name = 'V_832',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_799})

V_833 = Vertex(name = 'V_833',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_536,(0,1):C.GC_1193})

V_834 = Vertex(name = 'V_834',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_801})

V_835 = Vertex(name = 'V_835',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_549,(0,1):C.GC_1206})

V_836 = Vertex(name = 'V_836',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_827})

V_837 = Vertex(name = 'V_837',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_547,(0,1):C.GC_1204})

V_838 = Vertex(name = 'V_838',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_823})

V_839 = Vertex(name = 'V_839',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_548,(0,1):C.GC_1205})

V_840 = Vertex(name = 'V_840',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_825})

V_841 = Vertex(name = 'V_841',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_543,(0,1):C.GC_1200})

V_842 = Vertex(name = 'V_842',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_815})

V_843 = Vertex(name = 'V_843',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_541,(0,1):C.GC_1198})

V_844 = Vertex(name = 'V_844',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_811})

V_845 = Vertex(name = 'V_845',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_542,(0,1):C.GC_1199})

V_846 = Vertex(name = 'V_846',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_813})

V_847 = Vertex(name = 'V_847',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_546,(0,1):C.GC_1203})

V_848 = Vertex(name = 'V_848',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_821})

V_849 = Vertex(name = 'V_849',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_544,(0,1):C.GC_1201})

V_850 = Vertex(name = 'V_850',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_817})

V_851 = Vertex(name = 'V_851',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_545,(0,1):C.GC_1202})

V_852 = Vertex(name = 'V_852',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_819})

V_853 = Vertex(name = 'V_853',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_558,(0,1):C.GC_1215})

V_854 = Vertex(name = 'V_854',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_845})

V_855 = Vertex(name = 'V_855',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_556,(0,1):C.GC_1213})

V_856 = Vertex(name = 'V_856',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_841})

V_857 = Vertex(name = 'V_857',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_557,(0,1):C.GC_1214})

V_858 = Vertex(name = 'V_858',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_843})

V_859 = Vertex(name = 'V_859',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_552,(0,1):C.GC_1209})

V_860 = Vertex(name = 'V_860',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_833})

V_861 = Vertex(name = 'V_861',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_550,(0,1):C.GC_1207})

V_862 = Vertex(name = 'V_862',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_829})

V_863 = Vertex(name = 'V_863',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_551,(0,1):C.GC_1208})

V_864 = Vertex(name = 'V_864',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_831})

V_865 = Vertex(name = 'V_865',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_555,(0,1):C.GC_1212})

V_866 = Vertex(name = 'V_866',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_839})

V_867 = Vertex(name = 'V_867',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_553,(0,1):C.GC_1210})

V_868 = Vertex(name = 'V_868',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_835})

V_869 = Vertex(name = 'V_869',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_554,(0,1):C.GC_1211})

V_870 = Vertex(name = 'V_870',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_837})

V_871 = Vertex(name = 'V_871',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_567,(0,1):C.GC_1224})

V_872 = Vertex(name = 'V_872',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_863})

V_873 = Vertex(name = 'V_873',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_565,(0,1):C.GC_1222})

V_874 = Vertex(name = 'V_874',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_859})

V_875 = Vertex(name = 'V_875',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_566,(0,1):C.GC_1223})

V_876 = Vertex(name = 'V_876',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_861})

V_877 = Vertex(name = 'V_877',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_561,(0,1):C.GC_1218})

V_878 = Vertex(name = 'V_878',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_851})

V_879 = Vertex(name = 'V_879',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_559,(0,1):C.GC_1216})

V_880 = Vertex(name = 'V_880',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_847})

V_881 = Vertex(name = 'V_881',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_560,(0,1):C.GC_1217})

V_882 = Vertex(name = 'V_882',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_849})

V_883 = Vertex(name = 'V_883',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_564,(0,1):C.GC_1221})

V_884 = Vertex(name = 'V_884',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_857})

V_885 = Vertex(name = 'V_885',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_562,(0,1):C.GC_1219})

V_886 = Vertex(name = 'V_886',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_853})

V_887 = Vertex(name = 'V_887',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_563,(0,1):C.GC_1220})

V_888 = Vertex(name = 'V_888',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_855})

V_889 = Vertex(name = 'V_889',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_576,(0,1):C.GC_1233})

V_890 = Vertex(name = 'V_890',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_881})

V_891 = Vertex(name = 'V_891',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_574,(0,1):C.GC_1231})

V_892 = Vertex(name = 'V_892',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_877})

V_893 = Vertex(name = 'V_893',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_575,(0,1):C.GC_1232})

V_894 = Vertex(name = 'V_894',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_879})

V_895 = Vertex(name = 'V_895',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_570,(0,1):C.GC_1227})

V_896 = Vertex(name = 'V_896',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_869})

V_897 = Vertex(name = 'V_897',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_568,(0,1):C.GC_1225})

V_898 = Vertex(name = 'V_898',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_865})

V_899 = Vertex(name = 'V_899',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_569,(0,1):C.GC_1226})

V_900 = Vertex(name = 'V_900',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_867})

V_901 = Vertex(name = 'V_901',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_573,(0,1):C.GC_1230})

V_902 = Vertex(name = 'V_902',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_875})

V_903 = Vertex(name = 'V_903',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_571,(0,1):C.GC_1228})

V_904 = Vertex(name = 'V_904',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_871})

V_905 = Vertex(name = 'V_905',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_572,(0,1):C.GC_1229})

V_906 = Vertex(name = 'V_906',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_873})

V_907 = Vertex(name = 'V_907',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_585,(0,1):C.GC_1242})

V_908 = Vertex(name = 'V_908',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_899})

V_909 = Vertex(name = 'V_909',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_583,(0,1):C.GC_1240})

V_910 = Vertex(name = 'V_910',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_895})

V_911 = Vertex(name = 'V_911',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_584,(0,1):C.GC_1241})

V_912 = Vertex(name = 'V_912',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_897})

V_913 = Vertex(name = 'V_913',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_579,(0,1):C.GC_1236})

V_914 = Vertex(name = 'V_914',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_887})

V_915 = Vertex(name = 'V_915',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_577,(0,1):C.GC_1234})

V_916 = Vertex(name = 'V_916',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_883})

V_917 = Vertex(name = 'V_917',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_578,(0,1):C.GC_1235})

V_918 = Vertex(name = 'V_918',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_885})

V_919 = Vertex(name = 'V_919',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_582,(0,1):C.GC_1239})

V_920 = Vertex(name = 'V_920',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_893})

V_921 = Vertex(name = 'V_921',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_580,(0,1):C.GC_1237})

V_922 = Vertex(name = 'V_922',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_889})

V_923 = Vertex(name = 'V_923',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_581,(0,1):C.GC_1238})

V_924 = Vertex(name = 'V_924',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_891})

V_925 = Vertex(name = 'V_925',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_594,(0,1):C.GC_1251})

V_926 = Vertex(name = 'V_926',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_917})

V_927 = Vertex(name = 'V_927',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_592,(0,1):C.GC_1249})

V_928 = Vertex(name = 'V_928',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_913})

V_929 = Vertex(name = 'V_929',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_593,(0,1):C.GC_1250})

V_930 = Vertex(name = 'V_930',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_915})

V_931 = Vertex(name = 'V_931',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_588,(0,1):C.GC_1245})

V_932 = Vertex(name = 'V_932',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_905})

V_933 = Vertex(name = 'V_933',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_586,(0,1):C.GC_1243})

V_934 = Vertex(name = 'V_934',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_901})

V_935 = Vertex(name = 'V_935',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_587,(0,1):C.GC_1244})

V_936 = Vertex(name = 'V_936',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_903})

V_937 = Vertex(name = 'V_937',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_591,(0,1):C.GC_1248})

V_938 = Vertex(name = 'V_938',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_911})

V_939 = Vertex(name = 'V_939',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_589,(0,1):C.GC_1246})

V_940 = Vertex(name = 'V_940',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_907})

V_941 = Vertex(name = 'V_941',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_590,(0,1):C.GC_1247})

V_942 = Vertex(name = 'V_942',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_909})

V_943 = Vertex(name = 'V_943',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1842})

V_944 = Vertex(name = 'V_944',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1860})

V_945 = Vertex(name = 'V_945',
               particles = [ P.vm__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1843})

V_946 = Vertex(name = 'V_946',
               particles = [ P.vm__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1862})

V_947 = Vertex(name = 'V_947',
               particles = [ P.vt__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1844})

V_948 = Vertex(name = 'V_948',
               particles = [ P.vt__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1864})

V_949 = Vertex(name = 'V_949',
               particles = [ P.ve__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1845})

V_950 = Vertex(name = 'V_950',
               particles = [ P.ve__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1866})

V_951 = Vertex(name = 'V_951',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1846})

V_952 = Vertex(name = 'V_952',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1868})

V_953 = Vertex(name = 'V_953',
               particles = [ P.vt__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1847})

V_954 = Vertex(name = 'V_954',
               particles = [ P.vt__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1870})

V_955 = Vertex(name = 'V_955',
               particles = [ P.ve__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1848})

V_956 = Vertex(name = 'V_956',
               particles = [ P.ve__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1872})

V_957 = Vertex(name = 'V_957',
               particles = [ P.vm__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1849})

V_958 = Vertex(name = 'V_958',
               particles = [ P.vm__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1874})

V_959 = Vertex(name = 'V_959',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1850})

V_960 = Vertex(name = 'V_960',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1876})

V_961 = Vertex(name = 'V_961',
               particles = [ P.vm__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1925})

V_962 = Vertex(name = 'V_962',
               particles = [ P.vm__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1944})

V_963 = Vertex(name = 'V_963',
               particles = [ P.vt__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1926})

V_964 = Vertex(name = 'V_964',
               particles = [ P.vt__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1946})

V_965 = Vertex(name = 'V_965',
               particles = [ P.ve__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1927})

V_966 = Vertex(name = 'V_966',
               particles = [ P.ve__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1948})

V_967 = Vertex(name = 'V_967',
               particles = [ P.vt__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1929})

V_968 = Vertex(name = 'V_968',
               particles = [ P.vt__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1952})

V_969 = Vertex(name = 'V_969',
               particles = [ P.ve__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1930})

V_970 = Vertex(name = 'V_970',
               particles = [ P.ve__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1954})

V_971 = Vertex(name = 'V_971',
               particles = [ P.vm__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1931})

V_972 = Vertex(name = 'V_972',
               particles = [ P.vm__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1956})

V_973 = Vertex(name = 'V_973',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS6 ],
               couplings = {(0,0):C.GC_1842,(0,1):C.GC_1896,(0,2):C.GC_1450})

V_974 = Vertex(name = 'V_974',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS6 ],
               couplings = {(0,0):C.GC_1861,(0,1):C.GC_1503})

V_975 = Vertex(name = 'V_975',
               particles = [ P.mu__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_1843,(0,2):C.GC_1897,(0,1):C.GC_1453,(0,3):C.GC_1451})

V_976 = Vertex(name = 'V_976',
               particles = [ P.mu__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1863,(0,1):C.GC_1506,(0,2):C.GC_1504})

V_977 = Vertex(name = 'V_977',
               particles = [ P.ta__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_1844,(0,2):C.GC_1898,(0,1):C.GC_1456,(0,3):C.GC_1452})

V_978 = Vertex(name = 'V_978',
               particles = [ P.ta__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1865,(0,1):C.GC_1509,(0,2):C.GC_1505})

V_979 = Vertex(name = 'V_979',
               particles = [ P.e__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_1845,(0,2):C.GC_1899,(0,1):C.GC_1451,(0,3):C.GC_1453})

V_980 = Vertex(name = 'V_980',
               particles = [ P.e__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1867,(0,1):C.GC_1504,(0,2):C.GC_1506})

V_981 = Vertex(name = 'V_981',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS6 ],
               couplings = {(0,0):C.GC_1846,(0,1):C.GC_1900,(0,2):C.GC_1454})

V_982 = Vertex(name = 'V_982',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS6 ],
               couplings = {(0,0):C.GC_1869,(0,1):C.GC_1507})

V_983 = Vertex(name = 'V_983',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_1847,(0,2):C.GC_1901,(0,1):C.GC_1457,(0,3):C.GC_1455})

V_984 = Vertex(name = 'V_984',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1871,(0,1):C.GC_1510,(0,2):C.GC_1508})

V_985 = Vertex(name = 'V_985',
               particles = [ P.e__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_1848,(0,2):C.GC_1902,(0,1):C.GC_1452,(0,3):C.GC_1456})

V_986 = Vertex(name = 'V_986',
               particles = [ P.e__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1873,(0,1):C.GC_1505,(0,2):C.GC_1509})

V_987 = Vertex(name = 'V_987',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_1849,(0,2):C.GC_1903,(0,1):C.GC_1455,(0,3):C.GC_1457})

V_988 = Vertex(name = 'V_988',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1875,(0,1):C.GC_1508,(0,2):C.GC_1510})

V_989 = Vertex(name = 'V_989',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS6 ],
               couplings = {(0,0):C.GC_1850,(0,1):C.GC_1904,(0,2):C.GC_1458})

V_990 = Vertex(name = 'V_990',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS6 ],
               couplings = {(0,0):C.GC_1877,(0,1):C.GC_1511})

V_991 = Vertex(name = 'V_991',
               particles = [ P.mu__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,0):C.GC_1925,(0,2):C.GC_1979,(0,1):C.GC_1591,(0,3):C.GC_1589})

V_992 = Vertex(name = 'V_992',
               particles = [ P.mu__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1945,(0,1):C.GC_1728,(0,2):C.GC_1726})

V_993 = Vertex(name = 'V_993',
               particles = [ P.ta__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,0):C.GC_1926,(0,2):C.GC_1980,(0,1):C.GC_1594,(0,3):C.GC_1590})

V_994 = Vertex(name = 'V_994',
               particles = [ P.ta__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1947,(0,1):C.GC_1731,(0,2):C.GC_1727})

V_995 = Vertex(name = 'V_995',
               particles = [ P.e__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,0):C.GC_1927,(0,2):C.GC_1981,(0,1):C.GC_1589,(0,3):C.GC_1591})

V_996 = Vertex(name = 'V_996',
               particles = [ P.e__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1949,(0,1):C.GC_1726,(0,2):C.GC_1728})

V_997 = Vertex(name = 'V_997',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,0):C.GC_1929,(0,2):C.GC_1983,(0,1):C.GC_1595,(0,3):C.GC_1593})

V_998 = Vertex(name = 'V_998',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1953,(0,1):C.GC_1732,(0,2):C.GC_1730})

V_999 = Vertex(name = 'V_999',
               particles = [ P.e__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,0):C.GC_1930,(0,2):C.GC_1984,(0,1):C.GC_1590,(0,3):C.GC_1594})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.e__plus__, P.ta__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1955,(0,1):C.GC_1727,(0,2):C.GC_1731})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.mu__plus__, P.ta__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1931,(0,2):C.GC_1985,(0,1):C.GC_1593,(0,3):C.GC_1595})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.mu__plus__, P.ta__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1957,(0,1):C.GC_1730,(0,2):C.GC_1732})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1441})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1512})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.mu__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1444,(0,1):C.GC_1442})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.mu__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1515,(0,1):C.GC_1513})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.mu__plus__, P.e__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1582,(0,1):C.GC_1580})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.mu__plus__, P.e__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1737,(0,1):C.GC_1735})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.ta__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1447,(0,1):C.GC_1443})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.ta__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1518,(0,1):C.GC_1514})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.ta__plus__, P.e__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1585,(0,1):C.GC_1581})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.ta__plus__, P.e__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1740,(0,1):C.GC_1736})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.e__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1442,(0,1):C.GC_1444})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.e__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1513,(0,1):C.GC_1515})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.e__plus__, P.mu__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1580,(0,1):C.GC_1582})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.e__plus__, P.mu__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1735,(0,1):C.GC_1737})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1445})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1516})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.ta__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1448,(0,1):C.GC_1446})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.ta__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1519,(0,1):C.GC_1517})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.ta__plus__, P.mu__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1586,(0,1):C.GC_1584})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.ta__plus__, P.mu__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1741,(0,1):C.GC_1739})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.e__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1443,(0,1):C.GC_1447})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.e__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1514,(0,1):C.GC_1518})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.e__plus__, P.ta__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1581,(0,1):C.GC_1585})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.e__plus__, P.ta__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1736,(0,1):C.GC_1740})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.mu__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1446,(0,1):C.GC_1448})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.mu__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1517,(0,1):C.GC_1519})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.mu__plus__, P.ta__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1584,(0,1):C.GC_1586})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.mu__plus__, P.ta__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1739,(0,1):C.GC_1741})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1449})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1520})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1162,(0,0):C.GC_1635})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.mu__plus__, P.ve, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1163,(0,0):C.GC_1636})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.mu__plus__, P.ve, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV9 ],
                couplings = {(0,1):C.GC_1544,(0,0):C.GC_1744})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.ta__plus__, P.ve, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1164,(0,0):C.GC_1637})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.ta__plus__, P.ve, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV9 ],
                couplings = {(0,1):C.GC_1545,(0,0):C.GC_1745})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.e__plus__, P.vm, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1165,(0,0):C.GC_1638})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.e__plus__, P.vm, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV9 ],
                couplings = {(0,1):C.GC_1546,(0,0):C.GC_1746})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1166,(0,0):C.GC_1639})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.ta__plus__, P.vm, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1167,(0,0):C.GC_1640})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.ta__plus__, P.vm, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV9 ],
                couplings = {(0,1):C.GC_1548,(0,0):C.GC_1748})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.e__plus__, P.vt, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1168,(0,0):C.GC_1641})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.e__plus__, P.vt, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV9 ],
                couplings = {(0,1):C.GC_1549,(0,0):C.GC_1749})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.mu__plus__, P.vt, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1169,(0,0):C.GC_1642})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.mu__plus__, P.vt, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV9 ],
                couplings = {(0,1):C.GC_1550,(0,0):C.GC_1750})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS5 ],
                couplings = {(0,1):C.GC_1170,(0,0):C.GC_1643})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1162,(0,0):C.GC_1635})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1165,(0,0):C.GC_1636})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,1):C.GC_1546,(0,0):C.GC_1744})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1168,(0,0):C.GC_1637})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,1):C.GC_1549,(0,0):C.GC_1745})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1163,(0,0):C.GC_1638})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,1):C.GC_1544,(0,0):C.GC_1746})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1166,(0,0):C.GC_1639})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1169,(0,0):C.GC_1640})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,1):C.GC_1550,(0,0):C.GC_1748})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1164,(0,0):C.GC_1641})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,1):C.GC_1545,(0,0):C.GC_1749})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1167,(0,0):C.GC_1642})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,1):C.GC_1548,(0,0):C.GC_1750})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1, L.FFVS2 ],
                couplings = {(0,1):C.GC_1170,(0,0):C.GC_1643})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.c__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2601,(0,2):C.GC_1909,(0,1):C.GC_428,(0,3):C.GC_2564})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.c__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2602,(0,1):C.GC_1527,(0,2):C.GC_2567})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.t__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2603,(0,2):C.GC_1910,(0,1):C.GC_429,(0,3):C.GC_2565})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.t__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2604,(0,1):C.GC_1528,(0,2):C.GC_2568})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.u__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2599,(0,2):C.GC_1908,(0,1):C.GC_427,(0,3):C.GC_2563})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.u__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2600,(0,1):C.GC_1526,(0,2):C.GC_2566})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.c__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2902,(0,2):C.GC_1912,(0,1):C.GC_431,(0,3):C.GC_2865})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.c__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2903,(0,1):C.GC_1530,(0,2):C.GC_2868})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.t__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2904,(0,2):C.GC_1913,(0,1):C.GC_432,(0,3):C.GC_2866})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.t__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2905,(0,1):C.GC_1531,(0,2):C.GC_2869})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.u__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2900,(0,2):C.GC_1911,(0,1):C.GC_430,(0,3):C.GC_2864})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.u__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2901,(0,1):C.GC_1529,(0,2):C.GC_2867})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.c__tilde__, P.u, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2300,(0,2):C.GC_1906,(0,1):C.GC_425,(0,3):C.GC_2263})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.c__tilde__, P.u, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2301,(0,1):C.GC_1524,(0,2):C.GC_2266})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.t__tilde__, P.u, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2302,(0,2):C.GC_1907,(0,1):C.GC_426,(0,3):C.GC_2264})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.t__tilde__, P.u, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2303,(0,1):C.GC_1525,(0,2):C.GC_2267})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.u__tilde__, P.u, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_2298,(0,2):C.GC_1905,(0,1):C.GC_424,(0,3):C.GC_2262})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.u__tilde__, P.u, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2299,(0,1):C.GC_1523,(0,2):C.GC_2265})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.t__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_2612,(0,2):C.GC_1992,(0,1):C.GC_1784,(0,3):C.GC_2580})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.t__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2613,(0,1):C.GC_1829,(0,2):C.GC_2595})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.u__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_2608,(0,2):C.GC_1990,(0,1):C.GC_1782,(0,3):C.GC_2578})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.u__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2609,(0,1):C.GC_1827,(0,2):C.GC_2593})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.c__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_2911,(0,2):C.GC_1994,(0,1):C.GC_1786,(0,3):C.GC_2880})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.c__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2912,(0,1):C.GC_1831,(0,2):C.GC_2895})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.u__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_2909,(0,2):C.GC_1993,(0,1):C.GC_1785,(0,3):C.GC_2879})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.u__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2910,(0,1):C.GC_1830,(0,2):C.GC_2894})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.c__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_2309,(0,2):C.GC_1988,(0,1):C.GC_1780,(0,3):C.GC_2278})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.c__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2310,(0,1):C.GC_1825,(0,2):C.GC_2293})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.t__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_2311,(0,2):C.GC_1989,(0,1):C.GC_1781,(0,3):C.GC_2279})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.t__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2312,(0,1):C.GC_1826,(0,2):C.GC_2294})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.b__tilde__, P.b, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS3, L.FFVS6 ],
                couplings = {(0,0):C.GC_1859,(0,1):C.GC_1895,(0,2):C.GC_1440})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.b__tilde__, P.b, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS6 ],
                couplings = {(0,0):C.GC_1886,(0,1):C.GC_1493})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.d__tilde__, P.b, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_1857,(0,2):C.GC_1893,(0,1):C.GC_1434,(0,3):C.GC_1438})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.d__tilde__, P.b, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1884,(0,1):C.GC_1487,(0,2):C.GC_1491})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.s__tilde__, P.b, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_1858,(0,2):C.GC_1894,(0,1):C.GC_1437,(0,3):C.GC_1439})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.s__tilde__, P.b, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1885,(0,1):C.GC_1490,(0,2):C.GC_1492})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.b__tilde__, P.d, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_1853,(0,2):C.GC_1889,(0,1):C.GC_1438,(0,3):C.GC_1434})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.b__tilde__, P.d, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1880,(0,1):C.GC_1491,(0,2):C.GC_1487})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.d__tilde__, P.d, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS3, L.FFVS6 ],
                couplings = {(0,0):C.GC_1851,(0,1):C.GC_1887,(0,2):C.GC_1432})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.d__tilde__, P.d, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS6 ],
                couplings = {(0,0):C.GC_1878,(0,1):C.GC_1485})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.s__tilde__, P.d, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_1852,(0,2):C.GC_1888,(0,1):C.GC_1435,(0,3):C.GC_1433})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.s__tilde__, P.d, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1879,(0,1):C.GC_1488,(0,2):C.GC_1486})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.b__tilde__, P.s, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_1856,(0,2):C.GC_1892,(0,1):C.GC_1439,(0,3):C.GC_1437})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.b__tilde__, P.s, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1883,(0,1):C.GC_1492,(0,2):C.GC_1490})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.d__tilde__, P.s, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,0):C.GC_1854,(0,2):C.GC_1890,(0,1):C.GC_1433,(0,3):C.GC_1435})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.d__tilde__, P.s, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1881,(0,1):C.GC_1486,(0,2):C.GC_1488})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.s__tilde__, P.s, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS3, L.FFVS6 ],
                couplings = {(0,0):C.GC_1855,(0,1):C.GC_1891,(0,2):C.GC_1436})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.s__tilde__, P.s, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS6 ],
                couplings = {(0,0):C.GC_1882,(0,1):C.GC_1489})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.d__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1939,(0,2):C.GC_1975,(0,1):C.GC_1572,(0,3):C.GC_1576})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.d__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1966,(0,1):C.GC_1709,(0,2):C.GC_1713})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.s__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1940,(0,2):C.GC_1976,(0,1):C.GC_1575,(0,3):C.GC_1577})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.s__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1967,(0,1):C.GC_1712,(0,2):C.GC_1714})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.b__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1935,(0,2):C.GC_1971,(0,1):C.GC_1576,(0,3):C.GC_1572})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.b__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1962,(0,1):C.GC_1713,(0,2):C.GC_1709})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.s__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1934,(0,2):C.GC_1970,(0,1):C.GC_1573,(0,3):C.GC_1571})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.s__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1961,(0,1):C.GC_1710,(0,2):C.GC_1708})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.b__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1938,(0,2):C.GC_1974,(0,1):C.GC_1577,(0,3):C.GC_1575})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.b__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1965,(0,1):C.GC_1714,(0,2):C.GC_1712})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.d__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
                couplings = {(0,0):C.GC_1936,(0,2):C.GC_1972,(0,1):C.GC_1571,(0,3):C.GC_1573})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.d__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1963,(0,1):C.GC_1708,(0,2):C.GC_1710})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.c__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_419,(0,1):C.GC_2561})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.c__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1536,(0,1):C.GC_2570})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.t__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_420,(0,1):C.GC_2562})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.t__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1537,(0,1):C.GC_2571})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.t__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1775,(0,1):C.GC_2577})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.t__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1838,(0,1):C.GC_2598})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.u__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_418,(0,1):C.GC_2560})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.u__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1535,(0,1):C.GC_2569})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.u__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1773,(0,1):C.GC_2575})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.u__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1836,(0,1):C.GC_2596})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.c__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_422,(0,1):C.GC_2862})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.c__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1539,(0,1):C.GC_2871})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.c__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1777,(0,1):C.GC_2877})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.c__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1840,(0,1):C.GC_2898})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_423,(0,1):C.GC_2863})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1540,(0,1):C.GC_2872})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.u__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_421,(0,1):C.GC_2861})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.u__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1538,(0,1):C.GC_2870})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.u__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1776,(0,1):C.GC_2876})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.u__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1839,(0,1):C.GC_2897})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.c__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_416,(0,1):C.GC_2260})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.c__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1533,(0,1):C.GC_2269})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.c__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1771,(0,1):C.GC_2275})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.c__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1834,(0,1):C.GC_2296})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.t__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_417,(0,1):C.GC_2261})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.t__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1534,(0,1):C.GC_2270})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.t__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1772,(0,1):C.GC_2276})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.t__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1835,(0,1):C.GC_2297})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.u__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_415,(0,1):C.GC_2259})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.u__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1532,(0,1):C.GC_2268})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.b__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1431})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.b__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1502})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.d__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1425,(0,1):C.GC_1429})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.d__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1496,(0,1):C.GC_1500})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.d__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1563,(0,1):C.GC_1567})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.d__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1718,(0,1):C.GC_1722})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.s__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1428,(0,1):C.GC_1430})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.s__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1499,(0,1):C.GC_1501})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.s__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1566,(0,1):C.GC_1568})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.s__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1721,(0,1):C.GC_1723})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.b__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1429,(0,1):C.GC_1425})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.b__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1500,(0,1):C.GC_1496})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.b__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1567,(0,1):C.GC_1563})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.b__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1722,(0,1):C.GC_1718})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.d__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1423})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.d__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1494})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.s__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1426,(0,1):C.GC_1424})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.s__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1497,(0,1):C.GC_1495})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.s__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1564,(0,1):C.GC_1562})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.s__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1719,(0,1):C.GC_1717})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.b__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1430,(0,1):C.GC_1428})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.b__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1501,(0,1):C.GC_1499})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.b__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1568,(0,1):C.GC_1566})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.b__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1723,(0,1):C.GC_1721})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.d__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1424,(0,1):C.GC_1426})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.d__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1495,(0,1):C.GC_1497})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.d__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1562,(0,1):C.GC_1564})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.d__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1717,(0,1):C.GC_1719})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.s__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1427})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.s__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_1498})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1421,(0,3):C.GC_2424,(0,2):C.GC_1667,(0,0):C.GC_2586})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1415,(0,3):C.GC_2422,(0,2):C.GC_1665,(0,0):C.GC_2584})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1418,(0,3):C.GC_2423,(0,2):C.GC_1666,(0,0):C.GC_2585})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1422,(0,3):C.GC_2725,(0,2):C.GC_1670,(0,0):C.GC_2887})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1416,(0,3):C.GC_2723,(0,2):C.GC_1668,(0,0):C.GC_2885})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1419,(0,3):C.GC_2724,(0,2):C.GC_1669,(0,0):C.GC_2886})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1420,(0,3):C.GC_2123,(0,2):C.GC_1664,(0,0):C.GC_2285})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1414,(0,3):C.GC_2121,(0,2):C.GC_1662,(0,0):C.GC_2283})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_1417,(0,3):C.GC_2122,(0,2):C.GC_1663,(0,0):C.GC_2284})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_222,(0,3):C.GC_1421,(0,2):C.GC_1667,(0,0):C.GC_1802})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_333,(0,3):C.GC_1422,(0,2):C.GC_1670,(0,0):C.GC_1805})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_111,(0,3):C.GC_1420,(0,2):C.GC_1664,(0,0):C.GC_1799})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_220,(0,3):C.GC_1415,(0,2):C.GC_1665,(0,0):C.GC_1800})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_331,(0,3):C.GC_1416,(0,2):C.GC_1668,(0,0):C.GC_1803})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_109,(0,3):C.GC_1414,(0,2):C.GC_1662,(0,0):C.GC_1797})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_221,(0,3):C.GC_1418,(0,2):C.GC_1666,(0,0):C.GC_1801})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_332,(0,3):C.GC_1419,(0,2):C.GC_1669,(0,0):C.GC_1804})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
                couplings = {(0,1):C.GC_110,(0,3):C.GC_1417,(0,2):C.GC_1663,(0,0):C.GC_1798})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1598})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.vm__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1604})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.vt__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1610})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.ve__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1600})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1606})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.vt__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1612})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.ve__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1602})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.vm__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1608})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1614})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_1653})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.mu__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1656,(0,1):C.GC_1654})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.ta__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1659,(0,1):C.GC_1655})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.e__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1654,(0,1):C.GC_1656})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_1657})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.ta__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1660,(0,1):C.GC_1658})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.e__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1655,(0,1):C.GC_1659})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.mu__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1658,(0,1):C.GC_1660})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_1661})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1671})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1677})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1683})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1673})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1679})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1685})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1675})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1681})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_1687})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1629,(0,1):C.GC_2583})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1617,(0,1):C.GC_2581})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1623,(0,1):C.GC_2582})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1631,(0,1):C.GC_2884})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1619,(0,1):C.GC_2882})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1625,(0,1):C.GC_2883})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1627,(0,1):C.GC_2282})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1615,(0,1):C.GC_2280})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1621,(0,1):C.GC_2281})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1810,(0,1):C.GC_2588})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1811,(0,1):C.GC_2589})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1809,(0,1):C.GC_2587})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1813,(0,1):C.GC_2889})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1814,(0,1):C.GC_2890})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1812,(0,1):C.GC_2888})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1807,(0,1):C.GC_2287})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1808,(0,1):C.GC_2288})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1806,(0,1):C.GC_2286})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1704,(0,1):C.GC_2592})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1692,(0,1):C.GC_2590})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1698,(0,1):C.GC_2591})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1706,(0,1):C.GC_2893})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1694,(0,1):C.GC_2891})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1700,(0,1):C.GC_2892})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1702,(0,1):C.GC_2291})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1690,(0,1):C.GC_2289})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1696,(0,1):C.GC_2290})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1793,(0,1):C.GC_1630})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1796,(0,1):C.GC_1632})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1790,(0,1):C.GC_1628})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.c__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1791,(0,1):C.GC_1618})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1794,(0,1):C.GC_1620})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1788,(0,1):C.GC_1616})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1792,(0,1):C.GC_1624})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1795,(0,1):C.GC_1626})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.u__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1789,(0,1):C.GC_1622})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_1652})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1646,(0,1):C.GC_1650})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1649,(0,1):C.GC_1651})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1650,(0,1):C.GC_1646})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_1644})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1647,(0,1):C.GC_1645})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1651,(0,1):C.GC_1649})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1645,(0,1):C.GC_1647})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_1648})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1820,(0,1):C.GC_1703})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1823,(0,1):C.GC_1705})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1817,(0,1):C.GC_1701})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1818,(0,1):C.GC_1691})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1821,(0,1):C.GC_1693})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1815,(0,1):C.GC_1689})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1819,(0,1):C.GC_1697})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1822,(0,1):C.GC_1699})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV3 ],
                couplings = {(0,0):C.GC_1816,(0,1):C.GC_1695})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1597})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.mu__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1599})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.ta__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1601})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.e__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1603})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1605})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.ta__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1607})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.e__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1609})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.mu__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1611})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1613})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1672})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.mu__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1674})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.ta__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1676})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.e__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1678})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1680})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.ta__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1682})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.e__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1684})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.mu__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1686})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV3 ],
                couplings = {(0,0):C.GC_1688})

