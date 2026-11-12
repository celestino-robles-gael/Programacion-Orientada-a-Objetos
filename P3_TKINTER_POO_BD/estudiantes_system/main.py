from estudiantes import estudiantesBD
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Estudiantes")
        self.ventana.geometry("700x800")
        self.ventana.resizable(0,0)
        self.main()

    #   VISTAS del SISTEMA
    def borrarPantalla(self):
        for witget in self.ventana.winfo_children():
            witget.destroy()

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Estudiantes"
        Label(self.ventana, text = f"\n...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text = "1.- Agregar", command = self.insertar_view).pack(pady=5)
        Button(self.ventana, text = "2.- Borrar", command = self.eliminar_view).pack(pady=5)
        Button(self.ventana, text = "3.- Modificar", command = self.modificar_view).pack(pady=5)
        Button(self.ventana, text = "4.- Mostrar", command = self.mostrar_view).pack(pady=5)
        Button(self.ventana, text = "5.- Regresar", command = self.main).pack(pady=5)

    def main(self):
            self.borrarPantalla()
            Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
            Button(self.ventana, text = "1.- Estudiantes", command = self.menu_acciones).pack(pady=5)
            Button(self.ventana, text = "2.- Salir", command = self.ventana.quit).pack(pady=5)

    def insertar_view(self):
            self.borrarPantalla()
            Label(self.ventana, text = "...Ingresar los datos del estudiante...").pack(pady = 10)


            Label(self.ventana, text = "Nombre:").pack(pady = 5)
            self.nombre = Entry(self.ventana)
            self.nombre.focus()
            self.nombre.pack(pady = 5)

            Label(self.ventana, text = "Notas:").pack(pady = 5)
            self.nota = Entry(self.ventana)
            self.nota.pack(pady = 5)


            Button(self.ventana, text = "Guardar", command = self.insertar_controller).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def eliminar_view(self):
            self.borrarPantalla()
            Label(self.ventana, text = "...Ingresar el ID del estudiante a elimiar...").pack(pady = 10)

            Label(self.ventana, text = "ID:").pack(pady = 5)
            self.id = Entry(self.ventana)
            self.id.focus()
            self.id.pack(pady = 5)

            Button(self.ventana, text = "Eliminar", command = self.eliminar_controller).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def mostrar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Consultar los estudiantes...").pack(pady = 10)

        filas = ""
        filas = self.consultar_controller(filas)
        Label(self.ventana, text = f"{'NO.':<35}{'ID':<35}{'NOMBRE':<35}{'NOTA'}").pack(pady = 5)
        Label(self.ventana, text = f"{'-'*100}").pack(pady = 5)
        Label(self.ventana, text = f"{filas}").pack(pady = 5)

        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar el ID del estudiante a modificar...").pack(pady = 10)


        Label(self.ventana, text = "ID:").pack(pady = 5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady = 5)

        Label(self.ventana, text = "Nueva Nombre:").pack(pady = 5)
        self.nombre = Entry(self.ventana)
        self.nombre.pack(pady = 5)

        Label(self.ventana, text = "Nueva Nota:").pack(pady = 5)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady = 5)


        Button(self.ventana, text = "Guardar", command = self.modificar_controller).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)


    #   CONTROLADORES del SISTEMA
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title = "...Exitoso...", message = "...Accion realizada con exito...")
        else:
            messagebox.showerror(title = "...Verifica porfavor...", message = "...Esta accion no pudo realizarse...")
    
    def insertar_controller(self):
        estudiante1 = estudiantesBD.EstudiantesBD(self.nombre.get(), self.nota.get())
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1
        self.insertar_view()

    def eliminar_controller(self):
        id = self.id.get()
        respuesta = estudiantesBD.EstudiantesBD.eliminar(id)
        self.respuesta_sql(respuesta)

    def consultar_controller(self, filas):
        registros = estudiantesBD.EstudiantesBD.consultar()

        if len(registros) > 0:
            num_estudiantes = 1
            for fila in registros:
                filas=filas+f"\n{num_estudiantes:<20} \t {fila[0]:<20} \t {fila[1]:<20} \t {fila[2]}\n"

                num_estudiantes += 1
        else:
            filas=" NO existen datos que mostrar por el momento"

        return filas

    def modificar_controller(self):
        id = self.id.get()
        estudiante1 = estudiantesBD.EstudiantesBD(self.nombre.get(), self.nota.get())

        respuesta = estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1



    def datos_estudiantes(self, tipo):
        self.borrarPantalla()
        print(f"\n\t\t...Ingresa los datos del {tipo}...")

        estudiantitos = {}

        estudiantitos['nombre'] = input(
            "\t\tIngresa el nombre del estudiante: "
        ).strip().upper()

        estudiantitos['nota'] = float(
            input("\t\tIngresa la nota del estudiante: ").strip()
        )

        return estudiantitos

    def menu_estudiantes(self):
        opcion = True

        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")

            match opcion:
                case '1':
                    self.borrarPantalla()
                    estudiantitos = self.datos_estudiantes("estudiante")

                    estudiante1 = estudiantesBD.EstudiantesBD(
                        estudiantitos['nombre'],
                        estudiantitos['nota']
                    )

                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case '2':
                    self.borrarPantalla()

                    id_estudiante = int(
                        input("Ingresa el ID del estudiante a eliminar: ").strip()
                    )

                    respuesta = estudiantesBD.EstudiantesBD.eliminar(
                        id_estudiante
                    )
                    self.respuesta_sql(respuesta)

                case '3':
                    self.borrarPantalla()

                    id_estudiante = int(
                        input("Ingresa el ID del estudiante a actualizar: ").strip()
                    )

                    estudiantitos = self.datos_estudiantes("estudiante")

                    estudiante1 = estudiantesBD.EstudiantesBD(
                        estudiantitos['nombre'],
                        estudiantitos['nota']
                    )

                    respuesta = estudiante1.actualizar(id_estudiante)
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case '4':
                    self.borrarPantalla()
                    registros = estudiantesBD.EstudiantesBD.consultar()

                    if registros and len(registros) > 0:
                        num_estudiante = 1

                        for fila in registros:
                            print(
                                f"\n\t\t...::: Estudiante # {num_estudiante} :::..."
                            )
                            print(f"ID: {fila[0]}")
                            print(f"Nombre: {fila[1]}")
                            print(f"Nota: {fila[2]}")
                            num_estudiante += 1

                        self.esperarTecla()

                    else:
                        print("\n\n\t\tNo existen datos que mostrar por el momento.")
                        self.esperarTecla()

                case '5':
                    self.borrarPantalla()
                    print("\t\t...Regresando al menu principal...")
                    opcion = False

                case _:
                    input("\t\t\t...Opcion invalida...")

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()