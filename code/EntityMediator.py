from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod #08.02
    def verify_collision_window(ent: Entity): #Verificar se entidades estão dentro da janela do jogo
        if isinstance(ent, Enemy): #Se a instância for do tipo Enemy, faça...
            if ent.rect.right < 0: #Se o lado direito for menor que 0
                ent.health = 0 #health recebe 0

        if isinstance(ent, EnemyShot): #Se a instância for do tipo EnemyShot, faça...
            if ent.rect.right < 0: #Se o lado direito for menor que 0
                ent.health = 0 #health recebe 0

        if isinstance(ent, PlayerShot):  # Se a instância for do tipo PlayerShot, faça...
            if ent.rect.left < 0:  # Se o lado esquerdo for menor que 0
                ent.health = 0  # health recebe 0



    @staticmethod #08.03
    def verify_health(entity_list: list[Entity]):  # Verificar vida e remover quando zerar
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.give_score(ent, entity_list)
                entity_list.remove(ent)

    @staticmethod #08.06
    def verify_collision_entity(ent1, ent2): #Verificar colisões entre entidades
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def give_score(enemy: Enemy, entity_list: list[Entity]): #Coletar score
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

    @staticmethod #08.04
    def verify_collision(entity_list: list[Entity]): #Verificar colisões
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_collision_entity(entity1, entity2)


