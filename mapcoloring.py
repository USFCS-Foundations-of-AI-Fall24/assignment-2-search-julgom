from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

## colors: 0: Red, 1: Blue 2: Green
colors = {0 : 'Red',1:'Blue',2:'Green'}
## frequencies: : 0: f1, 1: f2 2: f3
frequencies = {0 : 'f1',1:'f2',2:'f3'}

SF = model.NewIntVar(0,2,'SF')
Alameda = model.NewIntVar(0,2,'Alameda')
Marin = model.NewIntVar(0,2,'Marin')
SanMateo = model.NewIntVar(0,2,'San Mateo')
SantaClara = model.NewIntVar(0,2,'Santa Clara')
ContraCosta = model.NewIntVar(0,2,'Contra Costa')
Solano = model.NewIntVar(0,2,'Solano')
Napa = model.NewIntVar(0,2,'Napa')
Sonoma = model.NewIntVar(0,2,'Sonoma')

Antenna_1 = model.NewIntVar(0,2,'A1')
Antenna_2  = model.NewIntVar(0,2,'A2')
Antenna_3  = model.NewIntVar(0,2,'A3')
Antenna_4  = model.NewIntVar(0,2,'A4')
Antenna_5  = model.NewIntVar(0,2,'A5')
Antenna_6  = model.NewIntVar(0,2,'A6')
Antenna_7  = model.NewIntVar(0,2,'A7')
Antenna_8  = model.NewIntVar(0,2,'A8')
Antenna_9  = model.NewIntVar(0,2,'A9')


#Antenna1 = model_2.NewIntVar(0,2, "A1")

## add edges
model.Add(SF != Alameda)
model.Add(SF != Marin)
model.Add(SF != SanMateo)
model.Add(ContraCosta != Alameda)
model.Add(Alameda != SanMateo)
model.Add(Alameda != SantaClara)
model.Add(SantaClara != SanMateo)
model.Add(Marin != Sonoma)
model.Add(Sonoma != Napa)
model.Add(Napa != Solano)
model.Add(Solano != ContraCosta)
model.Add(ContraCosta != Marin)

## add edges
model.Add(Antenna_1 != Antenna_2)
model.Add(Antenna_1 != Antenna_3)
model.Add(Antenna_1 != Antenna_4)

model.Add(Antenna_2 != Antenna_3)
model.Add(Antenna_2 != Antenna_4)
model.Add(Antenna_2 != Antenna_5)
model.Add(Antenna_2 != Antenna_6)

model.Add(Antenna_3 != Antenna_6)
model.Add(Antenna_3 != Antenna_9)

model.Add(Antenna_4 != Antenna_5)

model.Add(Antenna_6 != Antenna_7)
model.Add(Antenna_6 != Antenna_8)

model.Add(Antenna_7 != Antenna_8)

model.Add(Antenna_8 != Antenna_9)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("SF: %s" % colors[solver.Value(SF)])
    print("Alameda: %s" % colors[solver.Value(Alameda)])
    print("Marin: %s" % colors[solver.Value(Marin)])
    print("Contra Costa: %s" % colors[solver.Value(ContraCosta)])
    print("Solano: %s" % colors[solver.Value(Solano)])
    print("Sonoma: %s" % colors[solver.Value(Sonoma)])
    print("Santa Clara: %s" % colors[solver.Value(SantaClara)])
    print("San Mateo: %s" % colors[solver.Value(SanMateo)])
    print("Napa: %s" % colors[solver.Value(Napa)])
    print()
    print("Antenna 1: %s" % frequencies[solver.Value(Antenna_1)])
    print("Antenna 2: %s" % frequencies[solver.Value(Antenna_2)])
    print("Antenna 3: %s" % frequencies[solver.Value(Antenna_3)])
    print("Antenna 4: %s" % frequencies[solver.Value(Antenna_4)])
    print("Antenna 5: %s" % frequencies[solver.Value(Antenna_5)])
    print("Antenna 6: %s" % frequencies[solver.Value(Antenna_6)])
    print("Antenna 7: %s" % frequencies[solver.Value(Antenna_7)])
    print("Antenna 8: %s" % frequencies[solver.Value(Antenna_8)])
    print("Antenna 9: %s" % frequencies[solver.Value(Antenna_9)])
