def_test_list_union_method_returns_correct_result(self):
  demarcaciones = ["a.portero", "b.defensa", "c.mediocampista", "e.delantero"]
  print(demarcaciones)
  demarcaciones2 = sorted(demarcaciones, key=str.upper)
  print(demarcaciones2)
  demarcaciones.insert(3, "d.mediapunta")
  print(demarcaciones)
  demarcaciones.insert(6, "f.entrenador")
  print(demarcaciones)
  demarcaciones.pop([3])
  demarcaciones.remove("f.entrenador")
  demarcaciones.extend("g.presidente")
  print(demarcaciones)
