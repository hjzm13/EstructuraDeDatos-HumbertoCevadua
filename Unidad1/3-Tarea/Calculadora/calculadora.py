import tkinter as tk
from tkinter import ttk

# =========================================================
# #region LÓGICA
# =========================================================
class LogicaCalculadora:
    """
    Lógica pura de la calculadora (no conoce la UI).
    Expone callbacks para que la interfaz actualice el display e historial.
    """

    def __init__(self):
        # Estado interno
        self._acumulador: float = 0.0                  # Resultado parcial
        self._operador_pendiente: str = ""             # "+", "-", "*", "/"
        self._reiniciar_en_siguiente_digito: bool = True

        # Callbacks a la UI (inyectados desde la vista)
        self._cb_actualizar_display = None             # fn(str)
        self._cb_actualizar_historial = None           # fn(str)

        # Valor que “ve” la lógica en el display
        self._texto_display: str = "0"

    # ---------- Callbacks ----------
    def establecer_callback_display(self, fn):
        self._cb_actualizar_display = fn
        self._empujar_display()

    def establecer_callback_historial(self, fn):
        self._cb_actualizar_historial = fn
        self._empujar_historial()

    # ---------- Utilidades internas ----------
    def _valor_actual(self) -> float:
        try:
            return float(self._texto_display.replace(",", "."))
        except ValueError:
            return 0.0

    def _formato(self, numero: float) -> str:
        return str(int(numero)) if float(numero).is_integer() else str(numero)

    def _poner_display(self, texto: str) -> None:
        self._texto_display = texto
        self._empujar_display()

    def _empujar_display(self) -> None:
        if self._cb_actualizar_display:
            self._cb_actualizar_display(self._texto_display)

    def _empujar_historial(self) -> None:
        if self._cb_actualizar_historial:
            if self._operador_pendiente:
                simbolo = {"+": "+", "-": "−", "*": "×", "/": "÷"}[self._operador_pendiente]
                self._cb_actualizar_historial(f"{self._formato(self._acumulador)} {simbolo}")
            else:
                self._cb_actualizar_historial("")

    # ---------- API pública que usa la UI ----------
    def ingresar_digito(self, digito: str) -> None:
        if self._reiniciar_en_siguiente_digito or self._texto_display == "0":
            self._poner_display(digito)
            self._reiniciar_en_siguiente_digito = False
        else:
            self._poner_display(self._texto_display + digito)

    def ingresar_punto_decimal(self) -> None:
        if self._reiniciar_en_siguiente_digito:
            self._poner_display("0.")
            self._reiniciar_en_siguiente_digito = False
        elif "." not in self._texto_display:
            self._poner_display(self._texto_display + ".")

    def establecer_operador(self, operador: str) -> None:
        if self._operador_pendiente:
            self._resolver_operacion()
        else:
            self._acumulador = self._valor_actual()

        self._operador_pendiente = operador
        self._reiniciar_en_siguiente_digito = True
        self._empujar_historial()

    def calcular_resultado(self) -> None:
        self._resolver_operacion()
        self._operador_pendiente = ""
        self._reiniciar_en_siguiente_digito = True
        self._empujar_historial()

    def limpiar_entrada(self) -> None:
        self._poner_display("0")
        self._reiniciar_en_siguiente_digito = True

    def limpiar_todo(self) -> None:
        self._acumulador = 0.0
        self._operador_pendiente = ""
        self._poner_display("0")
        self._reiniciar_en_siguiente_digito = True
        self._empujar_historial()

    def cambiar_signo(self) -> None:
        valor = self._valor_actual()
        if valor != 0:
            self._poner_display(self._formato(-valor))

    def borrar_ultimo_caracter(self) -> None:
        if self._reiniciar_en_siguiente_digito:
            self._poner_display("0")
            return
        if len(self._texto_display) > 1:
            self._poner_display(self._texto_display[:-1])
        else:
            self._poner_display("0")
            self._reiniciar_en_siguiente_digito = True

    # ---------- Núcleo de cálculo ----------
    def _resolver_operacion(self) -> None:
        valor_derecha = self._valor_actual()
        try:
            if self._operador_pendiente == "+":
                self._acumulador += valor_derecha
            elif self._operador_pendiente == "-":
                self._acumulador -= valor_derecha
            elif self._operador_pendiente == "*":
                self._acumulador *= valor_derecha
            elif self._operador_pendiente == "/":
                if valor_derecha == 0:
                    raise ZeroDivisionError
                self._acumulador /= valor_derecha
            else:
                self._acumulador = valor_derecha

            self._poner_display(self._formato(self._acumulador))
        except ZeroDivisionError:
            self._poner_display("Error/0")
            self._acumulador = 0.0
            self._operador_pendiente = ""
            self._reiniciar_en_siguiente_digito = True
            self._empujar_historial()
# =========================================================
# #endregion LÓGICA
# =========================================================


# =========================================================
# #region UI (Tkinter): diseño y conexión con la lógica
# =========================================================
# Paleta y fuentes (tema oscuro)
COLOR_FONDO_VENTANA   = "#111318"
COLOR_TARJETA         = "#191c23"
COLOR_TEXTO           = "#e7e7ea"
COLOR_TEXTO_SUAVE     = "#9aa1ad"
COLOR_BOTON           = "#222632"
COLOR_BOTON_OPERADOR  = "#2a3142"
COLOR_BOTON_IGUAL     = "#2f6df4"

FUENTE_PANTALLA       = ("Segoe UI", 36)
FUENTE_SUBTITULO      = ("Segoe UI", 12)
FUENTE_BOTON          = ("Segoe UI", 14)

def construir_ui(raiz: tk.Tk, logica: LogicaCalculadora) -> None:
    """Arma toda la interfaz y conecta eventos con la lógica."""
    raiz.title("Calculadora")
    raiz.configure(bg=COLOR_FONDO_VENTANA)
    raiz.minsize(320, 420)

    # Contenedor principal
    marco_principal = ttk.Frame(raiz, padding=12)
    marco_principal.grid(sticky="nsew")
    raiz.rowconfigure(0, weight=1)
    raiz.columnconfigure(0, weight=1)

    # Estilos ttk
    estilos = ttk.Style()
    try:
        estilos.theme_use("clam")
    except tk.TclError:
        pass

    estilos.configure("TFrame", background=COLOR_FONDO_VENTANA)
    estilos.configure("Tarjeta.TFrame", background=COLOR_TARJETA, relief="flat")
    estilos.configure("Pantalla.TLabel", background=COLOR_TARJETA, foreground=COLOR_TEXTO,
                      font=FUENTE_PANTALLA, anchor="e")
    estilos.configure("Sub.TLabel", background=COLOR_TARJETA, foreground=COLOR_TEXTO_SUAVE,
                      font=FUENTE_SUBTITULO, anchor="e")
    estilos.configure("Tecla.TButton", font=FUENTE_BOTON, padding=6)
    estilos.configure("Oper.TButton", font=FUENTE_BOTON, padding=6)
    estilos.configure("Igual.TButton", font=FUENTE_BOTON, padding=6)

    # Tarjeta de display
    tarjeta = ttk.Frame(marco_principal, style="Tarjeta.TFrame", padding=12)
    tarjeta.grid(row=0, column=0, sticky="ew")
    marco_principal.columnconfigure(0, weight=1)

    etiqueta_historial = ttk.Label(tarjeta, text="", style="Sub.TLabel")
    etiqueta_historial.grid(row=0, column=0, sticky="ew")
    etiqueta_pantalla = ttk.Label(tarjeta, text="0", style="Pantalla.TLabel")
    etiqueta_pantalla.grid(row=1, column=0, sticky="ew")

    # Rejilla de botones
    rejilla = ttk.Frame(marco_principal)
    rejilla.grid(row=1, column=0, sticky="nsew", pady=(12, 0))
    for r in range(5):
        rejilla.rowconfigure(r, weight=1)
    for c in range(4):
        rejilla.columnconfigure(c, weight=1)

    # Helpers
    def aplicar_estilo_boton(boton: ttk.Button, tipo: str):
        color = (COLOR_BOTON if tipo == "tecla"
                 else COLOR_BOTON_OPERADOR if tipo == "oper"
                 else COLOR_BOTON_IGUAL)
        nombre_estilo = {"tecla": "Tecla.TButton", "oper": "Oper.TButton", "igual": "Igual.TButton"}[tipo]
        boton.configure(style=nombre_estilo, takefocus=False)
        boton.tk.call("ttk::style", "configure", nombre_estilo, "-background", color, "-foreground", COLOR_TEXTO)

    def agregar_boton(texto, fila, col, tipo="tecla", comando=None, span=1):
        b = ttk.Button(rejilla, text=texto, command=comando)
        b.grid(row=fila, column=col, columnspan=span, sticky="nsew", padx=4, pady=4)
        aplicar_estilo_boton(b, tipo)
        return b

    # Botones (conexión a lógica)
    agregar_boton("C",  0, 0, "oper", comando=logica.limpiar_todo)
    agregar_boton("CE", 0, 1, "oper", comando=logica.limpiar_entrada)
    agregar_boton("±",  0, 2, "oper", comando=logica.cambiar_signo)
    agregar_boton("÷",  0, 3, "oper", comando=lambda: logica.establecer_operador("/"))

    agregar_boton("7",  1, 0, comando=lambda: logica.ingresar_digito("7"))
    agregar_boton("8",  1, 1, comando=lambda: logica.ingresar_digito("8"))
    agregar_boton("9",  1, 2, comando=lambda: logica.ingresar_digito("9"))
    agregar_boton("×",  1, 3, "oper", comando=lambda: logica.establecer_operador("*"))

    agregar_boton("4",  2, 0, comando=lambda: logica.ingresar_digito("4"))
    agregar_boton("5",  2, 1, comando=lambda: logica.ingresar_digito("5"))
    agregar_boton("6",  2, 2, comando=lambda: logica.ingresar_digito("6"))
    agregar_boton("−",  2, 3, "oper", comando=lambda: logica.establecer_operador("-"))

    agregar_boton("1",  3, 0, comando=lambda: logica.ingresar_digito("1"))
    agregar_boton("2",  3, 1, comando=lambda: logica.ingresar_digito("2"))
    agregar_boton("3",  3, 2, comando=lambda: logica.ingresar_digito("3"))
    agregar_boton("+",  3, 3, "oper", comando=lambda: logica.establecer_operador("+"))

    agregar_boton("0",  4, 0, span=2, comando=lambda: logica.ingresar_digito("0"))
    agregar_boton(".",  4, 2, comando=logica.ingresar_punto_decimal)
    agregar_boton("=",  4, 3, "igual", comando=logica.calcular_resultado)

    # Conectar lógica → UI
    logica.establecer_callback_display(lambda texto: etiqueta_pantalla.config(text=texto))
    logica.establecer_callback_historial(lambda texto: etiqueta_historial.config(text=texto))

    # Atajos de teclado
    def manejar_tecla(e: tk.Event):
        ch = e.char
        if ch.isdigit():
            logica.ingresar_digito(ch)
        elif ch in "+-*/":
            logica.establecer_operador(ch)
        elif ch == ".":
            logica.ingresar_punto_decimal()

    raiz.bind("<Key>", manejar_tecla)
    raiz.bind("<Return>", lambda e: logica.calcular_resultado())
    raiz.bind("<BackSpace>", lambda e: logica.borrar_ultimo_caracter())
# =========================================================
# #endregion UI
# =========================================================


# =========================================================
# #region PUNTO DE ENTRADA
# =========================================================
def main():
    raiz = tk.Tk()
    logica = LogicaCalculadora()
    construir_ui(raiz, logica)
    raiz.mainloop()

if __name__ == "__main__":
    main()
# =========================================================
# #endregion
# =========================================================
