% База знаний об играх
% У игр есть: название, жанр, платформа, рейтинг
% Для запуска: ? - start.

game("The Witcher 3: Wild Hunt", rpg, pc, 9.8).
game("The Legend of Zelda: Breath of the Wild", adventure, switch, 9.7).
game("Grand Theft Auto V", action, ps4, 9.5).
game("Overwatch", shooter, xbox, 8.9).
game("Minecraft", sandbox, pc, 9.0).
game("Animal Crossing: New Horizons", simulation, switch, 9.6).
game("Red Dead Redemption 2", action_adventure, ps4, 9.8).
game("Fortnite", battle_royale, pc, 8.7).
game("League of Legends", moba, pc, 9.3).
game("FIFA 22", sports, ps5, 8.5).
game("Assassin's Creed Valhalla", action_rpg, xbox, 9.1).
game("Cyberpunk 2077", rpg, pc, 7.2).
game("Super Mario Odyssey", platformer, switch, 9.5).
game("Call of Duty: Warzone", battle_royale, ps4, 8.8).
game("Halo Infinite", shooter, xbox, 8.9).
game("Among Us", social_deduction, pc, 8.4).
game("The Last of Us Part II", action_adventure, ps4, 9.6).
game("Counter-Strike: Global Offensive", shooter, pc, 9.2).
game("Rainbow Six Siege", tactical_shooter, pc, 8.9).
game("Final Fantasy VII Remake", rpg, ps4, 9.0).
game("Apex Legends", battle_royale, pc, 8.7).

% Rules for recommending games based on preferences

% Рекомендация по жанру
recommend_by_genre(Genre, Game) :-
    game(Game, Genre, _, _).

% Рекомендация по платформе
recommend_by_platform(Platform, Game) :-
    game(Game, _, Platform, _).

% Рекомендация по платформе и жанру
recommendation(Genre, Platform, Game) :-
    recommend_by_genre(Genre, Game),
    recommend_by_platform(Platform, Game).

% Рекомендация по рейтингу (выведится равный или больше указанному)
recommend_by_rating(Rating, Game) :-
    game(Game, _, _, GameRating),
    GameRating >= Rating.

% Последняя рекомендация по всем критериям
final_recommendation(Genre, Platform, Rating, Game) :-
    recommendation(Genre, Platform, Game),
    recommend_by_rating(Rating, Game).

% Простой интерфейс для пользователя
recommend_by_genre_interface :-
    write('Enter the genre: '),
    read(Genre),
    nl,
    write('Recommended games of genre '), write(Genre), write(':'), nl,
    findall(Game, recommend_by_genre(Genre, Game), Games),
    print_games(Games),
    start.

recommend_by_platform_interface :-
    write('Enter the platform: '),
    read(Platform),
    nl,
    write('Recommended games for platform '), write(Platform), write(':'), nl,
    findall(Game, recommend_by_platform(Platform, Game), Games),
    print_games(Games),
    start.

recommendation_interface :-
    write('Enter the genre: '),
    read(Genre),
    nl,
    write('Enter the platform: '),
    read(Platform),
    nl,
    write('Recommended games of genre '), write(Genre), write(' for platform '), write(Platform), write(':'), nl,
    findall(Game, recommendation(Genre, Platform, Game), Games),
    print_games(Games),
    start.

final_recommendation_interface :-
    write('Enter the genre: '),
    read(Genre),
    nl,
    write('Enter the platform: '),
    read(Platform),
    nl,
    write('Enter the minimum rating: '),
    read(Rating),
    nl,
    write('Final recommendation:'), nl,
    findall(Game, final_recommendation(Genre, Platform, Rating, Game), Games),
    print_games(Games),
    start.

print_games([]).
print_games([Game|Games]) :-
    write('- '), write(Game), nl,
    print_games(Games).

% Флаг для отслеживания необходимости завершения программы
:- dynamic should_exit/0.

% Основной предикат для запуска интерфейса
start :-
    \+ should_exit,
    write('Welcome to the Game Recommendation System!'), nl,
    write('Choose an option:'), nl,
    write('1. Recommend games by genre'), nl,
    write('2. Recommend games by platform'), nl,
    write('3. Recommend games by genre and platform'), nl,
    write('4. Final recommendation'), nl,
    write('5. Exit'), nl,
    read(Choice),
    process_choice(Choice).

% Обработка выбора пользователя
process_choice(1) :-
    recommend_by_genre_interface.
process_choice(2) :-
    recommend_by_platform_interface.
process_choice(3) :-
    recommendation_interface.
process_choice(4) :-
    final_recommendation_interface.
process_choice(5) :-
    quit.

quit :-
    write('Goodbye!'), nl,
    assert(should_exit).

% Запуск интерфейса
:- start.