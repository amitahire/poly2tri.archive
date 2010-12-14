#!/usr/bin/env python2.7
from framework import Game, draw_polygon, reset_zoom, draw_line
from seidel import *

class Poly2Tri(Game):

    screen_size = 800.0, 600.0

    dude = [[174.50415,494.59368],[215.21844,478.87939],[207.36129,458.87939],[203.07558,441.02225],[203.07558,418.1651],
        [210.93272,394.59367],[224.50415,373.1651],[241.64701,358.1651],[257.36129,354.59367],[275.93272,356.73653],
        [293.07558,359.59367],[309.50415,377.45082],[322.36129,398.1651],[331.64701,421.73653],[335.21844,437.45082],
        [356.64701,428.52225],[356.1113,428.34367],[356.1113,428.34367],[368.78987,419.59368],[349.50415,384.59367],
        [323.78987,359.59367],[290.93272,343.87939],[267.36129,341.02225],[264.50415,331.02225],[264.50415,321.02225],
        [268.78987,306.02225],[285.93272,286.02225],[295.21844,270.30796],[303.78987,254.59367],[306.64701,213.87939],
        [320,202.36218],[265,202.36218],[286.64701,217.45082],[293.78987,241.02225],[285,257.36218],[270.93272,271.73653],
        [254.50415,266.02225],[250.93272,248.1651],[256.64701,233.1651],[256.64701,221.02225],[245.93272,215.30796],
        [238.78987,216.73653],[233.78987,232.45082],[232.36129,249.59367],[243.07558,257.09367],[242.89701,270.30796],
        [235.93272,279.95082],[222.36129,293.1651],[205.21844,300.6651],[185,297.36218],[170,242.36218],[175,327.36218],
        [185,322.36218],[195,317.36218],[230.75415,301.02225],[235.39701,312.45082],[240.57558,323.52225],
        [243.61129,330.48653],[245.21844,335.12939],[245.03987,344.4151],[229.86129,349.4151],[209.14701,362.09367],
        [192.89701,377.80796],[177.18272,402.27225],[172.36129,413.87939],[169.14701,430.48653],[168.61129,458.52225],
        [168.61129,492.80796]]
    
    test = [[235.04275999999999, 739.07534999999996], [218.13066000000001, 719.73902999999996], 
            [218.15215000000001, 709.96821], [218.17362, 700.19740000000002], [243.15215000000001, 685.27858000000003], 
            [268.13065, 670.35974999999996], [268.13065, 660.81429000000003], [268.13065, 651.26882999999998],
            [314.55921999999998, 651.26882999999998], [360.98779000000002, 651.26882999999998], 
            [360.98683999999997, 666.44740000000002], [360.98046561000007, 669.27438118000009], 
            [360.96234088000011,672.68539864000013], [360.93345946999995, 676.58895225999993], 
            [360.89481504000003, 680.89354191999996], [360.84740125000002, 685.50766749999991], 
            [360.79221175999999, 690.33982888000003], [360.73024022999999, 695.29852593999999], 
            [360.66248032000004, 700.29225856000005], [360.58992569000003, 705.22952662000012],          
            [360.51357000000002, 710.01882999999998], [360.04131999999998, 738.41168000000005],
            [310.51454999999999, 738.41168000000005], [260.98779999999999, 738.41168000000005], 
            [260.98779999999999, 748.41168000000005], [260.98779999999999, 758.41168000000005], 
            [256.47133000000002, 758.41168000000005], [251.95484999999999, 758.41168000000005]]
    
    test2 = [[101.25, 1006.8145], [-0.0, 869.65629999999999], [0.012800000000000001, 630.57820000000004], 
		[0.025600000000000001, 391.5], [13.7628, 385.74239999999998], [20.536000000000001, 382.96260000000001], 
		[26.871200000000002, 380.49279999999999],[32.864100000000001, 378.30540000000002], 
		[38.610700000000001, 376.37279999999998], [44.206600000000002, 374.66730000000001], 
		[49.747799999999998, 373.16129999999998], [55.329900000000002, 371.82709999999997], 
		[61.0488, 370.63720000000001],[67.000299999999996, 369.56400000000002], [73.280299999999997, 368.5797], 
		[77.521299999999997, 368.07459999999998], [82.578500000000005, 367.66539999999998], 
		[88.263199999999998, 367.35390000000001], [94.386899999999997, 367.14170000000001], 
		[100.7611, 367.0308], [107.1972, 367.02269999999999], [113.5067, 367.11930000000001], 
		[119.5009, 367.32229999999998], [124.9913, 367.63339999999999], [129.7894, 368.05450000000002], 
		[136.77860000000001, 368.94200000000001], [143.9999, 370.10390000000001], [151.3793, 371.52069999999998], 
		[158.84270000000001, 373.17270000000002], [166.3159, 375.04050000000001], [173.72499999999999, 377.10449999999997], 
		[180.9957, 379.34500000000003], [188.0539, 381.74250000000001], [194.82570000000001, 384.27749999999997], 
		[201.23679999999999, 386.93029999999999], [212.5, 391.83980000000003], [212.08760000000001, 550.41989999999998], 
		[211.67509999999999, 709.0], [274.00200000000001, 709.0], [336.3288, 709.0], [335.66520000000003, 636.25], 
		[335.55739999999997, 623.91790000000003], [335.45409999999998, 611.09199999999998], [335.3569, 598.0163], 
		[335.267, 584.93499999999995], [335.18599999999998, 572.09220000000005], [335.11540000000002, 559.73199999999997], 
		[335.0566, 548.09860000000003], [335.0111, 537.43600000000004], [334.98039999999997, 527.98839999999996], 
		[334.96589999999998, 520.0], [334.93029999999999, 476.5], [264.0222, 418.0], [193.114, 359.5], 
		[193.05699999999999, 295.4984], [193.0, 231.49680000000001], [308.7516, 115.7484], [424.50319999999999, 0.0], 
		[430.71390000000002, -0.0], [436.9246, -0.0], [458.9753, 20.0], [481.02589999999998, 40.0], 
		[558.38530000000003, 40.0], [635.74469999999997, 40.0], [660.50120000000004, 19.9588], 
		[685.25779999999997, -0.082400000000000001], [692.0471, 0.20880000000000001], 
		[698.8365, 0.5], [809.42550000000006, 115.9161], [920.01459999999997, 231.3321], [919.75729999999999, 295.3526], 
		[919.5, 359.37310000000002], [850.31790000000001, 416.4366], [781.13589999999999, 473.5], 
		[781.06790000000001, 593.7577], [781.0, 714.0154], [842.25, 713.7577], [903.5, 713.5], [903.5, 552.5], [903.5, 391.5],
		[915.5, 386.2894], [925.01319999999998, 382.34390000000002], [934.29579999999999, 378.88010000000003], 
		[943.42060000000004, 375.8827], [952.46050000000002,373.33629999999999], [961.48839999999996, 371.22570000000002], 
		[970.57719999999995, 369.53559999999999], [979.79989999999998, 368.25069999999999], 
		[989.22929999999997, 367.35570000000001], [998.9384, 366.83539999999999], [1009.0, 366.67430000000002], 
		[1018.876, 366.87939999999998], [1028.7419, 367.4649], [1038.5688, 368.42529999999999], 
		[1048.3277, 369.75490000000002], [1057.9897000000001, 371.44799999999998], [1067.5259000000001, 373.49900000000002],
		[1076.9074000000001, 375.90219999999999], [1086.1052, 378.65210000000002], [1095.0904, 381.74290000000002],
		[1103.8340000000001, 385.16899999999998], [1105.4327000000001, 385.83539999999999], 
		[1107.0215000000001, 386.49689999999998], [1108.5744999999999, 387.1429], [1110.0654999999999, 387.76240000000001], 
		[1111.4684, 388.34469999999999], [1112.7573, 388.87900000000002], [1113.9059, 389.3544], 
		[1114.8883000000001, 389.76010000000002], [1115.6784, 390.08530000000002], [1116.25, 390.3193], 
		[1119.0, 391.43849999999998], [1118.9577999999999, 633.4692], [1118.9155000000001, 875.5],[1016.0895, 1009.5], 
		[913.26340000000005, 1143.5], [908.63170000000002, 1143.8047999999999], [904.0, 1144.1096], [904.0, 993.0548], 
		[904.0, 842.0], [842.5, 842.0], [781.0, 842.0], [781.0, 918.5], [781.0, 995.0], [758.5, 995.0], 
		[753.20910000000003, 995.00739999999996], [748.79459999999995, 995.03269999999998], 
		[745.18129999999996, 995.08109999999999], [742.29399999999998, 995.15729999999996], 
		[740.05730000000005, 995.26639999999998], [738.39599999999996, 995.41330000000005],
		[737.23490000000004, 995.60289999999998], [736.49869999999999, 995.84010000000001], 
		[736.11210000000005, 996.13], [736.0, 996.47739999999999], [736.09749999999997, 996.82140000000004], 
		[736.42740000000003, 997.11329999999998], [737.04610000000002, 997.3587], [738.01009999999997, 997.56290000000001], 
		[739.37559999999996, 997.73140000000001], [741.19910000000004, 997.86959999999999], [743.53679999999997, 997.9828], 
		[746.44510000000002, 998.07659999999998], [749.98040000000003,998.15629999999999], 
		[754.19910000000004, 998.22739999999999], [772.39829999999995, 998.5], [823.72850000000005, 1071.0], 
		[875.05859999999996, 1143.5], [558.86419999999998, 1143.7516000000001], [507.74619999999999, 1143.787], 
		[459.17950000000002, 1143.8106], [413.82889999999998, 1143.8226], [372.35939999999999, 1143.8232], 
		[335.43560000000002, 1143.8130000000001], [303.7226, 1143.7919999999999], [277.88499999999999, 1143.7606000000001], 
		[258.58789999999999, 1143.7192], [246.49590000000001, 1143.6679999999999], [242.2739, 1143.6072999999999], 
		[244.95830000000001, 1139.4844000000001], [252.41210000000001, 1128.4439], [263.45999999999998, 1112.2019], 
		[276.92660000000001, 1092.4740999999999], [291.63650000000001, 1070.9766], [306.41430000000003, 1049.4251999999999], 
		[320.0847, 1029.5360000000001], [331.47219999999999, 1013.0247000000001], [339.4015, 1001.6074], 
		[342.69729999999998, 997.0], [342.98259999999999, 996.91470000000004], [343.6619, 996.82510000000002], 
		[344.70080000000002, 996.7328], [346.06450000000001, 996.63959999999997], [347.71870000000001, 996.54729999999995], 
		[349.62880000000001, 996.45770000000005], [351.76029999999997, 996.37249999999995], 
		[354.07859999999999, 996.29349999999999], [356.54919999999998, 996.22249999999997], [359.1377, 996.16110000000003], 
		[363.04469999999998, 996.07169999999996], [366.26229999999998, 995.97929999999997], 
		[368.85410000000002, 995.87580000000003], [370.88319999999999, 995.75319999999999], 
		[372.41320000000002, 995.60320000000002], [373.50729999999999,995.41790000000003], 
		[374.22899999999998, 995.18920000000003], [374.64159999999998, 994.90880000000004], 
		[374.80860000000001, 994.56889999999999], [374.79329999999999, 994.16110000000003], 
		[374.63619999999997, 993.7568], [374.2833, 993.4194], [373.65809999999999, 993.14160000000004], 
		[372.6841, 992.91570000000002], [371.28500000000003, 992.73419999999999], [369.3843, 992.58960000000002], 
		[366.90559999999999, 992.47429999999997], [363.77249999999998, 992.38059999999996], 
		[359.90839999999997, 992.30119999999999], [355.2371, 992.22839999999997], [336.0, 991.95680000000004], 
		[336.0, 914.97839999999997], [336.0, 838.0], [274.0, 838.0], [212.0, 838.0], [212.0, 991.0], [212.0, 1144.0], 
		[207.25, 1143.9864], [202.5, 1143.9727]]

    test3 = [[-5, 5],[-3, 0],[-5, -5],[5, -5],[5, 5]]
    test4 = [[5, 5],[5, -5],[-5, -5],[-3, 0],[-5, 5]]
    
    def __init__(self):
        super(Poly2Tri, self).__init__(*self.screen_size)       
        
        # Load point set
        file_name = "../data/star.dat"
        self.points = self.test3 #self.load_points(file_name) 
        
        # Triangulate
        t1 = self.time
        seidel = Triangulator(self.points)
        dt = (self.time - t1) * 1000.0
        
        self.triangles = seidel.triangles()
        self.trapezoids = seidel.trapezoids
        #self.trapezoids = seidel.trapezoidal_map.map
        self.edges = seidel.edge_list
        print "time (ms) = %f  , num triangles = %d" % (dt, len(self.triangles))
        
        for p in self.dude:
            p[0] -= 300
          
        '''
        make_ccw(self.dude)
        self.decomp_poly = []
        t1 = self.time
        decompose_poly(self.dude, self.decomp_poly)
        dt = (self.time - t1) * 1000.0
        print "time (ms) = %f  , num polies = %d" % (dt, len(self.decomp_poly))
        '''
      
        self.main_loop()
        
    def update(self):
        pass
        
    def render(self):
    
        reset_zoom(25, (0, 0), self.screen_size)
        red = 255, 0, 0
        yellow = 255, 255, 0
        green = 0, 255, 0
        
        for t in self.triangles:
          #t = self.triangles[0]
          draw_polygon(t, red)
        
        #for p in self.decomp_poly:
        #    draw_polygon(p, red)
        
        '''
        for t in self.trapezoids:
          #t = self.trapezoids[0]
          #verts = self.trapezoids[t].vertices()
          verts = t.vertices()
          draw_polygon(verts, yellow)
           
        for e in self.edges:
            p1 = e.p.x, e.p.y
            p2 = e.q.x, e.q.y
            draw_line(p1, p2, green)
        '''
        
    def load_points(self, file_name):
        infile = open(file_name, "r")
        points = []
        while infile:
            line = infile.readline()
            s = line.split()
            if len(s) == 0:
                break
            points.append((float(s[0]), float(s[1])))
        return points
        
if __name__ == '__main__':
    demo = Poly2Tri()