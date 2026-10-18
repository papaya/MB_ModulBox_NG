#!/usr/bin/env python3
"""Recharge les zones ET supprime les îlots de cuivre isolés (isolated_copper).
Usage: python de KiCad + refill_zones.py <pcb> [islands]
"""
import sys
import pcbnew

def refill(pcb_path, remove_islands=False):
    print("Chargement:", pcb_path)
    board = pcbnew.LoadBoard(pcb_path)
    zones = board.Zones()
    print("Zones trouvées:", len(zones))
    if remove_islands:
        for z in zones:
            try:
                z.SetIslandRemovalMode(pcbnew.ISLAND_REMOVAL_MODE_ALWAYS)
            except AttributeError:
                try:
                    z.SetRemoveIslands(True)
                except Exception:
                    print("  (mode îlots non supporté)")
        print("Suppression des îlots isolés activée")
    filler = pcbnew.ZONE_FILLER(board)
    ok = filler.Fill(zones)
    print("Remplissage:", "OK" if ok else "ECHEC")
    board.BuildConnectivity()
    pcbnew.SaveBoard(pcb_path, board)
    print("Sauvegardé:", pcb_path)

if __name__ == '__main__':
    refill(sys.argv[1], remove_islands=(len(sys.argv) > 2 and sys.argv[2] == 'islands'))
