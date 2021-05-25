def_test_list_union_method_returns_correct_result(self):
  lista = ["a.portero", "b.defensa", "c.mediocampista", "d.delantero"]
  self.assertEqual(lista[0], "a.portero")
  self.assertEqual(lista[0], "a.portero")
  lista.extend(["f.suplentes", "g.entrenador"])
  self.assertEqual(lista[-1], "g.entrenador")
  lista.insert(4, "da.mediapuntacentral")
  self.assertEqual(lista[4], "da.mediapuntacentral")
  self.assertEqual(4, lista.index("da.mediapuntacentral"))
  lista.remove("da.mediapuntacentral")
  self.assertEqual(["a.portero", "b.defensa","c.mediocampista","da.mediapuntacentral", "d.delantero"])
