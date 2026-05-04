#1Protocole de Routage
    #1.1Rappel
        #Adresse IP : 4 octets (32 bits) séparés par des points
        #Masque de sous-réseau : 4 octets (32 bits) séparés par des points
        #ID de réseau : adresse IP & masque de sous-réseau
        #Nb de hôte possible : 2^n - 2 (n = nombre de bits pour les hôtes)
        
        #router : appareil qui connecte plusieurs réseaux et achemine les paquets de données entre eux
        #route : chemin suivi par les paquets de données pour atteindre leur destination
        #table de routage : table utilisée par les routeurs pour déterminer le chemin à suivre pour acheminer les paquets de données
        
    #2Procole RIP (Routing Information Protocol)
        #RIP (vecteur de distance) — chaque routeur partage ce qu'il "connaît" à ses voisins. 
        # Simple mais limité à 15 sauts maximum. Algo : Bellman-Ford.

    #3Protocole OSPF (Open Shortest Path First)
        #OSPF (état de lien) — chaque routeur connaît la carte complète du réseau et calcule lui-même le meilleur chemin. 
        # Plus rapide, supporte les grands réseaux, mais plus complexe à configurer. Algo : Dijkstra.
        
    
  
        
        
        
        