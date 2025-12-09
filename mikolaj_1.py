import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- GŁÓWNA FUNKCJA RYSOWANIA ---

def draw_santa(face_color, show_gifts_left, show_gifts_right):
    
    # Konfiguracja wykresu (tworzymy figurę i osie)
    fig, ax = plt.subplots(figsize=(8, 10))
    
    # Ustawienia osi
    ax.set_aspect('equal')
    ax.set_xlim(-15, 15)
    ax.set_ylim(-25, 12)
    ax.axis('off') # Ukrywamy osie
    
    # --- ZDEFINIOWANE KOLORY ---
    RED_SUIT = 'red'
    WHITE_FUR = 'white'
    BLACK_LINES = 'black'
    GOLD = 'gold'
    
    # --- 1. CZAPKA ---
    ax.add_patch(patches.Polygon([(-3.5, 1.5), (3.5, 1.5), (0, 8)], closed=True,
                                 facecolor=RED_SUIT, edgecolor=BLACK_LINES, linewidth=1))
    ax.add_patch(patches.Rectangle((-4.5, 0.5), 9, 1, facecolor=WHITE_FUR, edgecolor=BLACK_LINES, linewidth=1))
    ax.add_patch(patches.Circle((0, 8.5), 1, facecolor=WHITE_FUR, edgecolor=BLACK_LINES, linewidth=1))

    # --- 2. GŁOWA I TWARZ ---
    # KOLOR TWARZY POBIERANY Z PARAMETRU STREAMLIT
    ax.add_patch(patches.Circle((0, -0.5), 4, facecolor=face_color, edgecolor=BLACK_LINES, linewidth=1, zorder=3))

    # Oczy (zorder=4)
    ax.add_patch(patches.Circle((-1.8, 1.2), 0.4, facecolor=BLACK_LINES, edgecolor=BLACK_LINES, linewidth=1, zorder=4))
    ax.add_patch(patches.Circle((1.8, 1.2), 0.4, facecolor=BLACK_LINES, edgecolor=BLACK_LINES, linewidth=1, zorder=4))

    # Nos (zorder=4)
    ax.add_patch(patches.Circle((0, 0), 0.8, facecolor='red', edgecolor=BLACK_LINES, linewidth=1, zorder=4))

    # Usta (zorder=4)
    ax.add_patch(patches.Arc((0, -1.5), 4, 2, angle=0, theta1=200, theta2=340,
                             edgecolor=BLACK_LINES, lw=2, capstyle='round', zorder=4))

    # Broda (zorder=2)
    broda_oval = patches.Ellipse((0, -5), 10, 10, angle=0, facecolor=WHITE_FUR, edgecolor=BLACK_LINES, linewidth=1, zorder=2)
    ax.add_patch(broda_oval)

    # --- 3. TUŁÓW, PAS, NOGI ---
    ax.add_patch(patches.Rectangle((-4.5, -13), 9, 13, facecolor=RED_SUIT, edgecolor=BLACK_LINES, linewidth=1)) # Tułów
    ax.add_patch(patches.Rectangle((-6.5, -9), 2, 4, facecolor=WHITE_FUR, edgecolor=BLACK_LINES, linewidth=1)) # Mankiet lewy
    ax.add_patch(patches.Rectangle((4.5, -9), 2, 4, facecolor=WHITE_FUR, edgecolor=BLACK_LINES, linewidth=1)) # Mankiet prawy
    ax.add_patch(patches.Circle((-6, -7), 1.2, facecolor=face_color, edgecolor=BLACK_LINES, linewidth=1, zorder=1)) # Dłoń lewa
    ax.add_patch(patches.Circle((6, -7), 1.2, facecolor=face_color, edgecolor=BLACK_LINES, linewidth=1, zorder=1)) # Dłoń prawa
    
    ax.add_patch(patches.Rectangle((-5.5, -10.5), 11, 2, facecolor=BLACK_LINES, edgecolor=BLACK_LINES, linewidth=1)) # Pas
    ax.add_patch(patches.Rectangle((-2.5, -11.5), 5, 4, facecolor=GOLD, edgecolor=BLACK_LINES, linewidth=1, zorder=1)) # Klamra
    ax.add_patch(patches.Rectangle((-1.5, -10.5), 3, 2, facecolor=BLACK_LINES, edgecolor=BLACK_LINES, linewidth=1, zorder=1)) # Otwór w klamrze

    ax.add_patch(patches.Rectangle((-3.5, -20), 3, 7, facecolor=RED_SUIT, edgecolor=BLACK_LINES, linewidth=1)) # Lewa noga
    ax.add_patch(patches.Rectangle((0.5, -20), 3, 7, facecolor=RED_SUIT, edgecolor=BLACK_LINES, linewidth=1)) # Prawa noga
    ax.add_patch(patches.Rectangle((-4, -22), 4, 2, facecolor=BLACK_LINES, edgecolor=BLACK_LINES, linewidth=1)) # Lewy but
    ax.add_patch(patches.Rectangle((0, -22), 4, 2, facecolor=BLACK_LINES, edgecolor=BLACK_LINES, linewidth=1)) # Prawy but

    # --- 4. PREZENTY (INTERAKTYWNE) ---
    
    if show_gifts_left:
        # Prezenty po lewej (czerwono-zielone)
        ax.add_patch(patches.Rectangle((-13, -22), 5, 5, facecolor='red', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((-11.5, -22), 2, 5, facecolor='green', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((-13, -19.5), 5, 2, facecolor='green', edgecolor=BLACK_LINES, linewidth=1))
        
        ax.add_patch(patches.Rectangle((-10, -18), 4, 4, facecolor='green', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((-8.8, -18), 1.5, 4, facecolor='red', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((-10, -16.8), 4, 1.5, facecolor='red', edgecolor=BLACK_LINES, linewidth=1))

    if show_gifts_right:
        # Prezenty po prawej (niebiesko-żółte)
        ax.add_patch(patches.Rectangle((8, -22), 5, 5, facecolor='blue', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((9.5, -22), 2, 5, facecolor='gold', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((8, -19.5), 5, 2, facecolor='gold', edgecolor=BLACK_LINES, linewidth=1))
        
        ax.add_patch(patches.Rectangle((7, -18), 4, 4, facecolor='blue', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((8.2, -18), 1.5, 4, facecolor='yellow', edgecolor=BLACK_LINES, linewidth=1))
        ax.add_patch(patches.Rectangle((7, -16.8), 4, 1.5, facecolor='yellow', edgecolor=BLACK_LINES, linewidth=1))

    # Zwracamy obiekt figury, aby Streamlit mógł go wyświetlić
    return fig

# --- GŁÓWNA STRUKTURA STREAMLIT ---

# 1. Panel boczny (Sidebar) do sterowania
st.sidebar.header("Ustawienia Mikołaja")

# Kontrolka 1: Kolor twarzy
# Początkowa wartość to beż: #FCDCB8
face_color_input = st.sidebar.color_picker(
    'Wybierz kolor twarzy:', 
    value='#FCDCB8'
)

# Kontrolki 2 i 3: Dodawanie/usuwanie prezentów
st.sidebar.header("Ustawienia Prezentów")
show_gifts_left_input = st.sidebar.checkbox('Pokaż prezenty Czerwono-Zielone (Lewa strona)', value=True)
show_gifts_right_input = st.sidebar.checkbox('Pokaż prezenty Niebiesko-Żółte (Prawa strona)', value=True)


# 2. Rysowanie i wyświetlanie na głównej stronie
st.title("Interaktywny Rysunek Świętego Mikołaja")
st.write("Użyj panelu bocznego (po lewej), aby zmienić kolor twarzy Mikołaja oraz ukryć/pokazać prezenty.")

# Wywołanie funkcji rysującej z wartościami pobranymi z interfejsu
st.pyplot(draw_santa(face_color_input, show_gifts_left_input, show_gifts_right_input))

# --- INSTRUKCJA URUCHOMIENIA ---
if st.sidebar.button("Jak uruchomić tę aplikację?"):
    st.sidebar.markdown(
        """
        1. **Zapisz** powyższy kod do pliku np. `mikolaj_interactive.py`.
        2. **Otwórz** terminal (w folderze z plikiem).
        3. **Uruchom** komendę:
           ```bash
           streamlit run mikolaj_interactive.py
           ```
        """
    )
