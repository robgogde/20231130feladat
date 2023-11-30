from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from collections.abc import Iterable


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def foglalas_felvetele(self, szobaszam, kezdo_datum, vegso_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if szoba.szabad_e(kezdo_datum, vegso_datum):
                    foglalas = Foglalas(szoba, kezdo_datum, vegso_datum)
                    szoba.foglalasok.append({'kezdo_datum': kezdo_datum, 'vegso_datum': vegso_datum})
                    self.foglalasok.append(foglalas)
                    return f"Szoba {szobaszam} foglalva lett {kezdo_datum.strftime('%Y-%m-%d')} - {vegso_datum.strftime('%Y-%m-%d')}. Az ár: {szoba.ar}."
                else:
                    return f"Szoba {szobaszam} már foglalt ezen a napon."
        return "Szoba nem található."

    def foglalas_lemondasa(self, szobaszam, kezdo_datum, vegso_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                szoba.foglalas_lemond(kezdo_datum, vegso_datum)
                return f"Sikeresen lemondta a foglalást a szobában {szobaszam} a következő időszakra: {kezdo_datum.strftime('%Y-%m-%d')} - {vegso_datum.strftime('%Y-%m-%d')}."
        return "Szoba nem található."

    def osszes_foglalas_listazasa(self):
        foglalasok_str_list = []
        for foglalas in self.foglalasok:
            szobaszam = foglalas.szoba.szobaszam
            kezdo_datum_str = foglalas.kezdo_datum.strftime('%Y-%m-%d')
            vegso_datum_str = foglalas.vegso_datum.strftime('%Y-%m-%d')
            foglalasok_str_list.append(f"Szoba {szobaszam} - {kezdo_datum_str} - {vegso_datum_str}")
        return ", ".join(foglalasok_str_list)


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalasok = []

    def szabad_e(self, kezdo_datum, vegso_datum):
        for foglalas in self.foglalasok:
            if foglalas['kezdo_datum'] <= kezdo_datum <= foglalas['vegso_datum'] or foglalas[
                'kezdo_datum'] <= vegso_datum <= foglalas['vegso_datum']:
                return False
        return True

    def foglalas_lemond(self, kezdo_datum, vegso_datum):
        self.foglalasok = [foglalas for foglalas in self.foglalasok if
                           foglalas['kezdo_datum'] != kezdo_datum or foglalas['vegso_datum'] != vegso_datum]

    def foglal(self, kezdo_datum, vegso_datum):
        if self.szabad_e(kezdo_datum, vegso_datum):
            self.foglalasok.append({'kezdo_datum': kezdo_datum, 'vegso_datum': vegso_datum})
            return f"Szoba {self.szobaszam} foglalva lett {kezdo_datum.strftime('%Y-%m-%d')} - {vegso_datum.strftime('%Y-%m-%d')}. Az ár: {self.ar}."
        else:
            return f"Szoba {self.szobaszam} már foglalt ezen a napon."

    def foglalasok_listazasa(self):
        foglalasok_str_list = []
        for foglalas in self.foglalasok:
            kezdo_datum_str = foglalas['kezdo_datum'].strftime('%Y-%m-%d')
            vegso_datum_str = foglalas['vegso_datum'].strftime('%Y-%m-%d')
            foglalasok_str_list.append(f"{kezdo_datum_str} - {vegso_datum_str}")
        return ", ".join(foglalasok_str_list)

    @abstractmethod
    def __str__(self):
        pass


class EgyagyasSzoba(Szoba):
    def __str__(self):
        foglalasok_str = self.foglalasok_listazasa()
        return f"Egyágyas szoba. A szoba száma: {self.szobaszam}, Ár: {self.ar}, Foglalások: {foglalasok_str if foglalasok_str else 'Nincsenek foglalások'}"


class KetagyasSzoba(Szoba):
    def __str__(self):
        foglalasok_str = self.foglalasok_listazasa()
        return f"Kétágyas szoba. A szoba száma: {self.szobaszam}, Ár: {self.ar}, Foglalások: {foglalasok_str if foglalasok_str else 'Nincsenek foglalások'}"


class Foglalas:
    def __init__(self, szoba, kezdo_datum, vegso_datum):
        self.szoba = szoba
        self.kezdo_datum = kezdo_datum
        self.vegso_datum = vegso_datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba: Szoba):
        self.szobak.append(szoba)

    def foglalas_felvetele(self, szobaszam, kezdo_datum, vegso_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if szoba.szabad_e(kezdo_datum, vegso_datum):
                    foglalas = Foglalas(szoba, kezdo_datum, vegso_datum)
                    szoba.foglalasok.append({'kezdo_datum': kezdo_datum, 'vegso_datum': vegso_datum})
                    self.foglalasok.append(foglalas)
                    return f"Szoba {szobaszam} foglalva lett {kezdo_datum.strftime('%Y-%m-%d')} - {vegso_datum.strftime('%Y-%m-%d')}. Az ár: {szoba.ar}."
                else:
                    return f"Szoba {szobaszam} már foglalt ezen a napon."
        return "Szoba nem található."

    def foglalas_lemondasa(self, szobaszam, kezdo_datum, vegso_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                szoba.foglalas_lemond(kezdo_datum, vegso_datum)
                return f"Sikeresen lemondta a foglalást a szobában {szobaszam} a következő időszakra: {kezdo_datum.strftime('%Y-%m-%d')} - {vegso_datum.strftime('%Y-%m-%d')}."
        return "Szoba nem található."

    def osszes_foglalas_listazasa(self):
        foglalasok_str_list = []
        for foglalas in self.foglalasok:
            szobaszam = foglalas.szoba.szobaszam
            kezdo_datum_str = foglalas.kezdo_datum.strftime('%Y-%m-%d')
            vegso_datum_str = foglalas.vegso_datum.strftime('%Y-%m-%d')
            foglalasok_str_list.append(f"Szoba {szobaszam} - {kezdo_datum_str} - {vegso_datum_str}")
        return ", ".join(foglalasok_str_list)

        # Felhasználói interfész és adatfeltöltés

    def foglalasi_folyamat(szalloda: Szalloda):
        while True:
            print("\nVálasszon műveletet:")
            print("1. Foglalás")
            print("2. Lemondás")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Adja meg a választott művelet sorszámát: ")

            if valasztas == "1":
                for szoba in szalloda.szobak:
                    print(f"Elérhető szoba: Szoba {szoba.szobaszam} - Ár: {szoba.ar} Ft")

                szobaszam = int(input("Adja meg a szobaszámot: "))

                kezdo_datum_str = input("Adja meg a kezdő dátumot (yyyy-mm-dd): ")
                kezdo_datum = datetime.strptime(kezdo_datum_str, '%Y-%m-%d')

                while True:
                    vegso_datum_str = input("Adja meg a végső dátumot (yyyy-mm-dd): ")
                    try:
                        vegso_datum = datetime.strptime(vegso_datum_str, '%Y-%m-%d')
                        break
                    except ValueError:
                        print("Érvénytelen dátum formátum. Kérjük, próbálja újra.")

                print(szalloda.foglalas_felvetele(szobaszam, kezdo_datum, vegso_datum))

            elif valasztas == "2":
                for szoba in szalloda.szobak:
                    print(f"Szoba {szoba.szobaszam} - Ár: {szoba.ar} Ft")

                szobaszam = int(input("Adja meg a szobaszámot: "))

                kezdo_datum_str = input("Adja meg a kezdő dátumot (yyyy-mm-dd): ")
                kezdo_datum = datetime.strptime(kezdo_datum_str, '%Y-%m-%d')

                while True:
                    vegso_datum_str = input("Adja meg a végső dátumot (yyyy-mm-dd): ")
                    try:
                        vegso_datum = datetime.strptime(vegso_datum_str, '%Y-%m-%d')
                        break
                    except ValueError:
                        print("Érvénytelen dátum formátum. Kérjük, próbálja újra.")

                print(szalloda.foglalas_lemondasa(szobaszam, kezdo_datum, vegso_datum))

            elif valasztas == "3":
                print(szalloda.osszes_foglalas_listazasa())

            elif valasztas == "4":
                print("Viszlát!")
                break

            else:
                print("Érvénytelen választás.")

    szalloda = Szalloda("Szálloda neve")
    szalloda.szoba_hozzaadas(EgyagyasSzoba(101, 50000))
    szalloda.szoba_hozzaadas(KetagyasSzoba(102, 60000))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(103, 55000))

    foglalasi_folyamat(szalloda)
