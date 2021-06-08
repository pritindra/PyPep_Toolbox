import sys
from simple_term_menu import TerminalMenu
from PepTool import *
from Bio.Seq import Seq
import os

def main():
    main_menu_title = "  PyPep Toolbox\n"
    main_menu_items = ["[p] Peptide sequencer","[o] Operation Menu", "Molecular Weight", "Amino acid count",
    "Isoelectric point","Charge at given pH","Molar Extinction Coefficient","[q] Quit","[h] Help"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_green", "bold")
    main_menu_style = ("bg_gray", "fg_green", "italics")
    main_menu_exit = False

    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    edit_menu_title = "  Menu 2\n"
    edit_menu_items = ["[p] Permutations", "amino_count", "get_amino_percent", "[q] Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    oper_menu_title = "  Operation Menu\n"
    oper_menu_items = ["[a]Add", "[m]Multiply by integer", "[c]Complement", "[C]Compare", "Hash", "[l]Add Sequence on left",
    "Non-overlapping count", "overlapping count", "Contains", "Find", "[q] Back to Main Menu"]
    oper_menu_back = False
    oper_menu = TerminalMenu(oper_menu_items,
                             oper_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()

                if edit_sel == 0:
                    patt = input("Enter the pattern::")
                    inp = input("Enter the inputs::")
                    X = PepTool(patt)

                    ch = input("Do you want to print output in a text file ?[y/n]")
                    if ch == "y":
                        file = open('output.txt', 'w')
                        sys.stdout = file
                        X.perm(inp)
                        file.close()
                    else:
                        X.perm(inp)

                elif edit_sel == 1:
                    patt = input("Enter the pattern::")
                    am = input("Enter the amino acid::")
                    X = PepTool(patt)
                    print(X.amino_count()[am])

                elif edit_sel == 2:
                    patt = input("Enter the pattern::")
                    am = input("Enter the amino acid::")
                    X = PepTool(patt)
                    print(X.get_amino_percent()[am])

                elif edit_sel == 3:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False

        elif main_sel == 1:
            while not oper_menu_back:
                oper_sel = oper_menu.show()

                if oper_sel == 0:
                    patt = input("Enter the sequence::")
                    inp = input("Enter other sequence::")
                    print("Added:: " + Seq(patt) + inp)

                elif oper_sel == 1:
                    patt = input("Enter the sequence::")
                    other = input("Enter the integer::")
                    print("Multiplied:: " + Seq(patt) * int(other))

                elif oper_sel == 2:
                    patt = input("Enter the sequence::")
                    print(Seq(patt).complement())

                elif oper_sel == 3:
                    patt = input("Enter the sequence::")
                    other = input("Another sequence::")
                    seq1 = Seq(patt)
                    seq2 = Seq(other)
                    if seq1 == seq2:
                        print("True")
                    else:
                        print("False")

                elif oper_sel == 4:
                    patt = input("Enter the sequence::")
                    return Seq(patt).hash()

                elif oper_sel == 5:
                    patt = input("Enter the sequence::")
                    inp = input("Enter other sequence::")
                    print("Added to left" + inp + Seq(patt))

                elif oper_sel == 6:
                    patt = input("Enter the sequence::")
                    sub = input("Enter the subsequence::")
                    print(Seq(patt).count(sub))

                elif oper_sel == 7:
                    patt = input("Enter the sequence::")
                    sub = input("Enter the subsequence::")
                    print(Seq(patt).count_overlap(sub))

                elif oper_sel == 8:
                    patt = input("Enter the sequence::")
                    sub = input("Enter the subsequence::")
                    sub in Seq(patt)

                elif oper_sel == 9:
                    patt = input("Enter the sequence::")
                    sub = input("Enter the subsequence::")
                    print(Seq(patt).find(sub))

                elif oper_sel == 10:
                    oper_menu_back = True
                    print("Back Selected")
            oper_menu_back = False


        elif main_sel == 2:
            patt = input("Enter the pattern::")
            X = PepTool(patt)
            print("The molecular weight of the sequence:: %0.2f" % X.molecular_weight())

        elif main_sel == 3:
            patt = input("Enter the pattern::")
            X = PepTool(patt)
            print(X.amino_count())

        elif main_sel == 4:
            patt = input("Enter the pattern::")
            X = PepTool(patt)
            print(X.isoelectric_point())

        elif main_sel == 5:
            patt = input("Enter the pattern::")
            ph = input("Enter the pH value::")
            X = PepTool(patt)
            print(X.charge_at_pH(float(ph)))

        elif main_sel == 6:
            patt = input("Enter the pattern::")
            X = PepTool(patt)
            print(X.molar_extinction_coefficient())

        elif main_sel == 7:
            main_menu_exit = True
            print("Quit Selected")

        elif main_sel == 8:
            os.system("cat help.txt")


if __name__ == "__main__":
    main()
