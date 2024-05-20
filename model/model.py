import copy


class Model:
    def __init__(self):
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzione = []

    def risolvi_quadrato(self, N):
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzione = []
        self._ricorsione([], set(range(1, N*N+1)), N)

    def _ricorsione(self, parziale, rimanenti, N):
        self._n_iterazioni += 1
        # caso terminale
        if len(parziale) == N*N:
            if self._is_soluzione_parziale(parziale,N):
                print(parziale)
                self._n_soluzioni += 1
                self._soluzione.append(copy.deepcopy(parziale))

        # caso ricorsivo
        else:
            for i in rimanenti:
                parziale.append(i)
                nuovi_rimanenti = copy.deepcopy(rimanenti)
                nuovi_rimanenti.remove(i)
                self._ricorsione(parziale, nuovi_rimanenti, N)
                parziale.pop()

    def _is_soluzione_parziale(self, parziale, N):
        numero_magico = N*(N*N+1)/2
        for row in range(N): # per ognina delle N righe
            somma = 0
            sottolista = parziale[row*N:(row+1)*N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        # Vincolo 2) colonne
        for col in range(0, N): # per ognina delle N righe
            somma = 0
            sottolista = parziale[col:((N-1)*N)+col+1:N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        # Vincolo 3) diagonale 1
        somma = 0
        for row_col in range(N):
            somma += parziale[row_col*N + row_col]
        if somma != numero_magico:
            return False

        # Vincolo 4) digonale 2
        somma = 0
        for row_col in range(N):
            somma += parziale[row_col * N + (N-1-row_col)]
        if somma != numero_magico:
            return False
        # tutti i vincoli soddisfatti
        return True

    def _is_soluzione(self, parziale, N):
        numero_magico = N*(N*N+1)/2
        n_righe = len(parziale) // N
        n_col = max(len(parziale) - N*N-1, 0)
        for row in range(n_righe): # per ognina delle N righe
            somma = 0
            sottolista = parziale[row*N:(row+1)*N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        # Vincolo 2) colonne
        for col in range(0, n_col): # per ognina delle N righe
            somma = 0
            sottolista = parziale[col:((N-1)*N)+col+1:N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        # Vincolo 3) diagonale 1
        somma = 0
        for row_col in range(N):
            somma += parziale[row_col*N + row_col]
        if somma != numero_magico:
            return False

        # Vincolo 4) digonale 2
        somma = 0
        for row_col in range(N):
            somma += parziale[row_col * N + (N-1-row_col)]
        if somma != numero_magico:
            return False
        # tutti i vincoli soddisfatti
        return True


    def stampa_soluzione(self, soluzione, N):
        print("-----------")
        for row in range(N):
            print([v for v in soluzione[row*N: (row+1)*N]])
        print("-----------")


if __name__ == '__main__':
    N = 3
    model = Model()
    model.risolvi_quadrato(N)
    print(f"Qaudrato di lato {N} risolto con {model._n_iterazioni} iterazioni ")
    print(f"Trovato {model._n_soluzioni} soluzioni ")
    for soluzione in model._soluzione:
        model.stampa_soluzione(soluzione, N)

