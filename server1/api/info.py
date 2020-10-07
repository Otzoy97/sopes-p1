class Info:
    def __init__(self, infoA, infoB):
        """infoA: info del servidor A. infoB: info del servidor B"""
        # determina el uso de cpu y ram
        infoA = infoA.json()["res"]
        infoB = infoB.json()["res"]
        # uso de cpu/ram A
        cpuA = infoA["cpu"]
        ramA = infoA["ram"]
        self.serverA = {"count": infoA["count"],"cpu": (cpuA["total"] - cpuA["idle"]) * (100/cpuA["total"]),
                        "ram": (ramA["total"] - ramA["free"] -
                                ramA["buffer"] - ramA["cached"]) * (100/ramA["total"])}
        # uso de cpu/ram B
        cpuB = infoB["cpu"]
        ramB = infoB["ram"]
        self.serverB = {"count": infoB["count"],"cpu": (cpuB["total"] - cpuB["idle"]) * (100/cpuB["total"]),
                        "ram": (ramB["total"] - ramB["free"] -
                                ramB["buffer"] - ramB["cached"]) * (100/ramB["total"])}
        
    def toServer(self):
        """Decide a cuál servidor enviar la información. 'A' para el servidor a, 'B' para el servidor b"""
        count = self.__getServerPerCount()
        if count == 'N':
            ram = self.__getServerPerRam()
            if ram == 'N':
                cpu = self.__getServerPerCpu()
                if cpu == 'N':
                    return 'A'
                return cpu
            return ram
        return count

    def __getServerPerCount(self):
        """Compara los cantidad de documentos en la bd del server a y b. El que tenga menor valor se elegirá. 'A' para server-a, 'B' para server-b y 'N' para ninguno"""
        if self.serverA["count"] < self.serverB["count"]:
            return 'A'
        elif self.serverA["count"] > self.serverB["count"]:
            return 'B'
        else:
            return 'N'

    def __getServerPerRam(self):
        """Compara los valores de ram del server a y b. El que tenga menor valor se elegirá. 'A' para server-a, 'B' para server-b y 'N' para ninguno"""
        if self.serverA["ram"] < self.serverB["ram"]:
            return 'A'
        elif self.serverA["ram"] > self.serverB["ram"]:
            return 'B'
        else:
            return 'N'

    def __getServerPerCpu(self):
        """Compara los valores de cpu del server a y b. El que tenga menor valor se elegirá. 'A' para server-a, 'B' para server-b y 'N' para ninguno"""
        if self.serverA["cpu"] < self.serverB["cpu"]:
            return 'A'
        elif self.serverA["cpu"] > self.serverB["cpu"]:
            return 'B'
        else:
            return 'N'        
