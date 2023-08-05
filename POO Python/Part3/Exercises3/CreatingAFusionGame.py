class Character():
    def __init__(self, name, damage, agility, defense, stamina):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.agility = agility
        self.stamina = stamina
        
    
    def __str__(self):
        return f'''Stats: 
-Name: {self.name}
-Damage: {self.damage}
-Agility: {self.agility}
-Defense: {self.defense}
-Stamina: {self.stamina}'''
    
    def __name(self, name, ch_name):
            x = round(len(name)/2)
            y = round(len(ch_name)/2)
            yy= len(ch_name)
            n_name = ''
            stop = 0
            for i in name:
                n_name += i
                stop += 1
                if stop >= x:
                    break
            n_ch_name = ''
            start = 0
            stop = 0
            for i in ch_name:
                start += 1
                if start > y:
                    n_ch_name += i
                    stop += 1
                if stop > y:
                    break
            new_name = n_name + n_ch_name
            return new_name
    
    def __add__(self, other):
        new_stat= lambda x, y: round(pow(((x + y)/2), 1.5))
        
                
        new_damage = new_stat(self.damage, other.damage)
        new_agility =  new_stat(self.agility, other.agility)
        new_defense = new_stat(self.defense, other.defense)
        new_stamina = new_stat(self.stamina, other.stamina)
        return Character(__name(self.name, other.name), new_damage, new_agility, new_defense, new_stamina)

Goku = Character('Goku', 999, 999, 999, 999)
Krilin = Character('Krilin', 100, 200, 10, 150)
Vegeta = Character('Vegeta', 50, 400, 600, 200)
fusion = Goku + Krilin 
print (fusion)


        
        
    