import math
import json

if True:
    words = ['float', 'kiosk', 'lithe', 'super', 'jazzy', 'haste', 'canon', 'voice', 'amuse', 'lumen', 'mango', 'growl', 'train', 'decry', 'blame', 'exile', 'shoal', 'wider', 'sorry', 'shook', 'cheek', 'fight', 'dusty', 'gorge', 'sheep', 'tepid', 'ditto', 'musty', 'guppy', 'graze', 'posit', 'worse', 'relay', 'delta', 'prize', 'cleat', 'vying', 'flail', 'debut', 'cinch', 'plate', 'which', 'upset', 'sheet', 'flour', 'clear', 'tacky', 'boast', 'carat', 'throw', 'spasm', 'sower', 'verge', 'shrug', 'waltz', 'bilge', 'retch', 'epoch', 'fuzzy', 'outgo', 'align', 'lathe', 'rupee', 'visit', 'stuck', 'nicer', 'furry', 'vault', 'tulip', 'onset', 'devil', 'wordy', 'arose', 'gonad', 'putty', 'clued', 'vivid', 'agape', 'solid', 'grime', 'moral', 'event', 'clove', 'acrid', 'stony', 'civil', 'ether', 'sport', 'refer', 'rajah', 'dicey', 'blush', 'right', 'kayak', 'denim', 'opine', 'award', 'spite', 'rover', 'splat', 'scrub', 'dogma', 'fairy', 'brush', 'waver', 'exist', 'glide', 'fetid', 'plump', 'woken', 'kneel', 'gaily', 'cabal', 'rabid', 'groin', 'marsh', 'shake', 'naval', 'awake', 'viral', 'cater', 'biddy', 'holly', 'ditch', 'deuce', 'repel', 'musky', 'micro', 'hovel', 'racer', 'climb', 'alike', 'welch', 'stink', 'siege', 'bonus', 'cedar', 'meter', 'scale', 'proxy', 'elide', 'jolly', 'vogue', 'stoic', 'gleam', 'whine', 'stick', 'filth', 'steer', 'scrum', 'thank', 'prowl', 'junta', 'mucus', 'lefty', 'scary', 'draft', 'borne', 'vapor', 'smash', 'mauve', 'wacky', 'happy', 'valet', 'penny', 'there', 'spied', 'never', 'equip', 'tooth', 'route', 'proof', 'curio', 'fried', 'weedy', 'timid', 'count', 'stein', 'frisk', 'murky', 'swift', 'fleet', 'clown', 'lyric', 'betel', 'gulch', 'water', 'melee', 'locus', 'abate', 'toxin', 'artsy', 'width', 'catch', 'drive', 'angry', 'month', 'blurt', 'liner', 'grimy', 'brawn', 'embed', 'drain', 'droop', 'usher', 'bravo', 'villa', 'acute', 'write', 'slant', 'shady', 'homer', 'carol', 'every', 'clung', 'vapid', 'flown', 'idiot', 'coach', 'condo', 'straw', 'ionic', 'crown', 'remit', 'merry', 'decor', 'beach', 'joust', 'green', 'lever', 'tutor', 'march', 'equal', 'dunce', 'guess', 'avian', 'claim', 'fluff', 'crazy', 'friar', 'quash', 'clean', 'purse', 'crest', 'pixie', 'quasi', 'cigar', 'pound', 'stone', 'caper', 'plush', 'randy', 'elude', 'smirk', 'theta', 'outer', 'daddy', 'carry', 'felon', 'older', 'clack', 'steed', 'dross', 'knack', 'mince', 'major', 'chock', 'gumbo', 'imbue', 'edict', 'leapt', 'yacht', 'swine', 'paler', 'livid', 'windy', 'bused', 'perch', 'shade', 'begat', 'sound', 'midst', 'payee', 'maker', 'towel', 'aware', 'beech', 'grunt', 'unfed', 'hello', 'tryst', 'mural', 'eking', 'zebra', 'freed', 'plunk', 'humor', 'leery', 'white', 'dingy', 'fudge', 'exult', 'skiff', 'anime', 'pagan', 'crawl', 'spoke', 'point', 'phase', 'piety', 'smear', 'imply', 'hutch', 'roast', 'berry', 'motif', 'leafy', 'dream', 'silky', 'watch', 'brink', 'flush', 'stock', 'poesy', 'gourd', 'emcee', 'spoil', 'slack', 'chant', 'infer', 'grief', 'visor', 'spare', 'aside', 'tumor', 'undid', 'swoop', 'empty', 'afire', 'shear', 'queue', 'frown', 'jumbo', 'flash', 'limit', 'sweet', 'bulky', 'forth', 'swami', 'begin', 'vaunt', 'unfit', 'hotel', 'tried', 'papal', 'crust', 'missy', 'cheat', 'spelt', 'lapse', 'glory', 'hairy', 'aroma', 'willy', 'oxide', 'pedal', 'trail', 'genie', 'croup', 'sniff', 'dirty', 'torus', 'twine', 'seedy', 'pluck', 'chump', 'odder', 'lymph', 'flirt', 'setup', 'pasty', 'scuba', 'krill', 'igloo', 'stole', 'index', 'inert', 'liege', 'union', 'demon', 'beset', 'order', 'belch', 'build', 'defer', 'lipid', 'snore', 'ovoid', 'scant', 'delve', 'spiky', 'steep', 'psalm', 'riper', 'nobly', 'stoke', 'niche', 'giddy', 'sewer', 'cavil', 'sieve', 'salve', 'tulle', 'karma', 'riser', 'belle', 'abbey', 'lucky', 'grant', 'gayly', 'blitz', 'shalt', 'chaos', 'dodgy', 'vodka', 'taker', 'pause', 'trope', 'lease', 'testy', 'druid', 'spike', 'outdo', 'koala', 'eager', 'angle', 'canoe', 'minor', 'moose', 'chute', 'elbow', 'still', 'renal', 'wooly', 'forum', 'sworn', 'spicy', 'prism', 'dally', 'novel', 'flick', 'joker', 'check', 'salty', 'sweep', 'sugar', 'fungi', 'stark', 'slash', 'floor', 'lapel', 'mulch', 'group', 'squib', 'child', 'wight', 'macro', 'rebut', 'donut', 'irony', 'cried', 'primo', 'purer', 'space', 'sunny', 'blink', 'tight', 'feign', 'pupil', 'offal', 'prime', 'squad', 'excel', 'least', 'mafia', 'legal', 'troop', 'rebus', 'troll', 'error', 'flock', 'chore', 'decay', 'saner', 'pinto', 'admin', 'skull', 'cream', 'fling', 'nerdy', 'lofty', 'broom', 'scoff', 'fiery', 'pithy', 'radar', 'epoxy', 'glove', 'mason', 'twist', 'stuff', 'basic', 'froze', 'greed', 'snide', 'inept', 'since', 'stool', 'spurn', 'leave', 'quilt', 'dopey', 'waist', 'refit', 'grass', 'piece', 'audio', 'matey', 'worry', 'bosom', 'dowel', 'aunty', 'grope', 'nudge', 'pence', 'gamut', 'taboo', 'quiet', 'gipsy', 'lemon', 'adorn', 'tunic', 'pesky', 'thrum', 'nomad', 'meaty', 'guard', 'under', 'untie', 'banal', 'cycle', 'ensue', 'poppy', 'style', 'loopy', 'human', 'layer', 'forte', 'table', 'sleep', 'twang', 'witty', 'apple', 'clank', 'fluke', 'stash', 'staff', 'unwed', 'prong', 'fable', 'mummy', 'phone', 'twixt', 'taper', 'manga', 'chord', 'shunt', 'safer', 'snaky', 'tubal', 'great', 'spine', 'raven', 'polyp', 'serum', 'opium', 'while', 'serif', 'whoop', 'spool', 'lumpy', 'tacit', 'story', 'suave', 'flung', 'tabby', 'loyal', 'cacao', 'filmy', 'annex', 'saute', 'bayou', 'sneer', 'buggy', 'rarer', 'think', 'chime', 'prune', 'overt', 'plumb', 'world', 'beard', 'larva', 'reedy', 'sooty', 'neigh', 'clump', 'ahead', 'spank', 'myrrh', 'choke', 'sword', 'clink', 'grout', 'depot', 'mossy', 'pushy', 'sauna', 'dance', 'voter', 'vista', 'crepe', 'truth', 'tawny', 'royal', 'price', 'grill', 'leant', 'quick', 'admit', 'pooch', 'crack', 'forgo', 'mercy', 'elegy', 'ethos', 'taint', 'elite', 'smack', 'stead', 'egret', 'itchy', 'decoy', 'issue', 'leaky', 'taffy', 'mania', 'lilac', 'chaff', 'quoth', 'drool', 'place', 'drier', 'crook', 'color', 'patty', 'baggy', 'macaw', 'dried', 'array', 'shuck', 'peach', 'gripe', 'suing', 'alert', 'river', 'kinky', 'mouse', 'shorn', 'mound', 'vowel', 'dress', 'nanny', 'rigid', 'limbo', 'slurp', 'filet', 'spoof', 'guava', 'crimp', 'tramp', 'mower', 'finer', 'shoot', 'along', 'cable', 'idler', 'bacon', 'tempo', 'total', 'brave', 'grown', 'onion', 'swell', 'swash', 'wafer', 'patsy', 'biome', 'dumpy', 'eater', 'ovate', 'bench', 'tying', 'nerve', 'dwarf', 'moldy', 'hound', 'hussy', 'sperm', 'wager', 'brook', 'spice', 'quite', 'alarm', 'pasta', 'purge', 'latte', 'tilde', 'fancy', 'vomit', 'stomp', 'facet', 'shard', 'melon', 'gland', 'asset', 'ruder', 'snare', 'chuck', 'argue', 'shout', 'smell', 'taken', 'cacti', 'oaken', 'steel', 'blurb', 'slush', 'broil', 'rider', 'laugh', 'mange', 'sleek', 'frank', 'farce', 'cubic', 'octal', 'salad', 'faint', 'terse', 'focus', 'endow', 'gusto', 'stood', 'sleet', 'ought', 'paper', 'inlay', 'snort', 'dairy', 'bushy', 'fresh', 'dingo', 'smock', 'wooer', 'conch', 'reign', 'hippo', 'thigh', 'blade', 'curse', 'privy', 'magma', 'snoop', 'batch', 'kebab', 'arson', 'shelf', 'plane', 'habit', 'lodge', 'threw', 'scold', 'urban', 'erupt', 'smith', 'baton', 'moult', 'study', 'party', 'rainy', 'enema', 'rumor', 'dusky', 'toddy', 'intro', 'glean', 'giant', 'beefy', 'inner', 'manor', 'venue', 'dowdy', 'regal', 'snuck', 'goose', 'creme', 'loamy', 'witch', 'tepee', 'avoid', 'agate', 'voila', 'brick', 'sonar', 'patch', 'batty', 'honor', 'clout', 'cease', 'mealy', 'timer', 'moody', 'fiend', 'muddy', 'prude', 'toxic', 'alien', 'bagel', 'bless', 'idyll', 'tenth', 'maize', 'agent', 'stilt', 'worst', 'crime', 'udder', 'loath', 'relic', 'slime', 'froth', 'swept', 'yearn', 'blown', 'trash', 'rehab', 'bluer', 'goody', 'class', 'amble', 'sadly', 'dilly', 'flout', 'thump', 'couch', 'scree', 'tenor', 'cyber', 'pulse', 'break', 'poise', 'cause', 'leggy', 'slink', 'slain', 'pulpy', 'rhino', 'maple', 'lance', 'synod', 'merit', 'axial', 'drama', 'eaten', 'shark', 'salvo', 'baron', 'humid', 'crash', 'crone', 'below', 'ennui', 'bleak', 'stork', 'rinse', 'other', 'torch', 'wrote', 'needy', 'wrist', 'scene', 'match', 'chair', 'marry', 'alpha', 'using', 'night', 'title', 'seven', 'aloof', 'masse', 'rural', 'might', 'foyer', 'snowy', 'moist', 'third', 'sandy', 'pride', 'waxen', 'recur', 'fizzy', 'erase', 'copse', 'fully', 'flume', 'brawl', 'pried', 'after', 'stave', 'front', 'merge', 'cache', 'smote', 'motto', 'tardy', 'recap', 'manly', 'tribe', 'stray', 'yield', 'angst', 'rebar', 'rayon', 'cobra', 'crisp', 'roomy', 'assay', 'tiger', 'slang', 'smart', 'brash', 'augur', 'shine', 'plaza', 'bitty', 'rigor', 'sense', 'qualm', 'above', 'noisy', 'final', 'lasso', 'coupe', 'quota', 'foamy', 'avail', 'amity', 'until', 'stall', 'omega', 'dealt', 'rerun', 'maxim', 'ebony', 'plank', 'swing', 'showy', 'plied', 'noble', 'bible', 'wield', 'wince', 'scour', 'shell', 'cumin', 'favor', 'swish', 'cabin', 'snarl', 'ninny', 'vouch', 'newly', 'elfin', 'acorn', 'girth', 'throb', 'brass', 'debug', 'cluck', 'husky', 'clock', 'chide', 'drawl', 'coyly', 'scarf', 'mammy', 'buddy', 'hatch', 'flank', 'cello', 'fatty', 'sight', 'rouge', 'gouge', 'vague', 'spore', 'coral', 'grand', 'colon', 'rocky', 'belie', 'joist', 'crier', 'boule', 'debar', 'adore', 'shush', 'borax', 'chick', 'feral', 'steak', 'baler', 'arrow', 'sixty', 'knife', 'strap', 'eagle', 'bevel', 'piney', 'diary', 'amass', 'otter', 'hasty', 'scone', 'finch', 'ovary', 'miser', 'shawl', 'shaky', 'vigil', 'sprig', 'hilly', 'unity', 'stale', 'blare', 'piano', 'shrew', 'tread', 'scoop', 'built', 'deter', 'risky', 'gamma', 'brunt', 'small', 'cagey', 'verse', 'edify', 'arise', 'movie', 'wryly', 'valor', 'blank', 'hunch', 'whiny', 'cocoa', 'credo', 'hobby', 'kitty', 'quill', 'steal', 'burnt', 'tally', 'adopt', 'buxom', 'raspy', 'fella', 'girly', 'scare', 'jerky', 'rower', 'metal', 'ficus', 'enter', 'gavel', 'harsh', 'spiny', 'frame', 'theft', 'cover', 'gruff', 'fruit', 'rugby', 'amiss', 'heave', 'unite', 'speed', 'lying', 'album', 'drone', 'gaunt', 'scion', 'fanny', 'fever', 'grape', 'latch', 'lager', 'leper', 'probe', 'knock', 'scorn', 'croak', 'squat', 'altar', 'bleep', 'brace', 'again', 'brisk', 'track', 'learn', 'loser', 'wrung', 'prick', 'crush', 'circa', 'hoist', 'banjo', 'salon', 'began', 'aglow', 'punch', 'ozone', 'angel', 'allot', 'nutty', 'covet', 'wheel', 'pansy', 'amply', 'peace', 'apron', 'trump', 'razor', 'motel', 'plume', 'essay', 'abase', 'siren', 'ruddy', 'force', 'fetal', 'bough', 'store', 'briar', 'lobby', 'scent', 'fiber', 'prior', 'geeky', 'charm', 'trite', 'extol', 'ninth', 'cheap', 'slate', 'ratio', 'range', 'flame', 'aphid', 'newer', 'leech', 'duchy', 'frill', 'aisle', 'model', 'young', 'blend', 'drape', 'hedge', 'bugle', 'viper', 'wrath', 'howdy', 'react', 'triad', 'maybe', 'first', 'crowd', 'eying', 'shack', 'strut', 'crick', 'wheat', 'bulge', 'ideal', 'grave', 'trawl', 'coven', 'abled', 'blood', 'jumpy', 'bigot', 'woozy', 'chalk', 'polka', 'quart', 'dowry', 'shock', 'orbit', 'conic', 'alibi', 'spend', 'brief', 'afoul', 'crank', 'tease', 'gaudy', 'would', 'dwell', 'crypt', 'topaz', 'balmy', 'slide', 'hater', 'linen', 'crate', 'puree', 'photo', 'spunk', 'teach', 'ghost', 'sully', 'preen', 'chafe', 'scowl', 'gnash', 'disco', 'tough', 'torso', 'yeast', 'boozy', 'smile', 'dolly', 'civic', 'groom', 'paddy', 'creed', 'woody', 'fault', 'olden', 'folio', 'fussy', 'tidal', 'aloft', 'foist', 'talon', 'cleft', 'stake', 'shift', 'slump', 'fetch', 'tasty', 'gooey', 'curly', 'rivet', 'crock', 'skimp', 'junto', 'sheer', 'whole', 'churn', 'spiel', 'china', 'rapid', 'bobby', 'drank', 'shirt', 'burly', 'trace', 'jetty', 'optic', 'pinky', 'lupus', 'later', 'widow', 'juicy', 'vixen', 'gazer', 'thorn', 'warty', 'filer', 'rebel', 'welsh', 'diner', 'waive', 'magic', 'ledge', 'liken', 'scram', 'budge', 'plaid', 'sloop', 'ferry', 'pouty', 'thing', 'swirl', 'haunt', 'sumac', 'polar', 'adapt', 'cloth', 'ridge', 'ranch', 'modem', 'exact', 'trout', 'lousy', 'comet', 'bribe', 'start', 'billy', 'petty', 'elect', 'lunch', 'rusty', 'frock', 'block', 'whiff', 'clang', 'birth', 'eject', 'ivory', 'champ', 'those', 'comic', 'evict', 'sonic', 'eerie', 'caddy', 'handy', 'tonic', 'among', 'whale', 'allow', 'grade', 'lanky', 'kneed', 'goner', 'mayor', 'tangy', 'false', 'elate', 'graph', 'bleat', 'amaze', 'doubt', 'rearm', 'ulcer', 'weird', 'pitch', 'baker', 'spell', 'bliss', 'canal', 'cling', 'undue', 'stout', 'diver', 'ripen', 'genre', 'paint', 'agree', 'alley', 'tweak', 'spook', 'clasp', 'retro', 'scalp', 'chasm', 'sinew', 'caste', 'decal', 'chest', 'weave', 'faith', 'silly', 'retry', 'candy', 'annoy', 'shank', 'rumba', 'beady', 'dizzy', 'anvil', 'swear', 'cough', 'amend', 'femur', 'bride', 'sassy', 'whisk', 'satyr', 'inbox', 'peril', 'glass', 'robot', 'ounce', 'storm', 'palsy', 'hoard', 'metro', 'flood', 'swill', 'plait', 'liver', 'flier', 'noise', 'twirl', 'stump', 'screw', 'hinge', 'grail', 'flesh', 'havoc', 'brine', 'swoon', 'patio', 'truly', 'aloud', 'comfy', 'brown', 'apart', 'going', 'hefty', 'north', 'woven', 'glyph', 'booty', 'ladle', 'libel', 'agile', 'flaky', 'frail', 'lunge', 'ocean', 'funny', 'halve', 'stage', 'mucky', 'vinyl', 'sushi', 'delay', 'lurid', 'flint', 'adobe', 'ghoul', 'heard', 'basal', 'singe', 'guild', 'cairn', 'token', 'staid', 'slunk', 'basil', 'court', 'humph', 'snake', 'chart', 'aping', 'puffy', 'semen', 'tipsy', 'azure', 'ovine', 'media', 'dirge', 'renew', 'stack', 'their', 'spear', 'spout', 'notch', 'money', 'blast', 'foray', 'snuff', 'sulky', 'board', 'mocha', 'smelt', 'ditty', 'solve', 'tower', 'crass', 'octet', 'hydro', 'ankle', 'quell', 'shale', 'video', 'drake', 'rival', 'thick', 'deign', 'adept', 'woman', 'sedan', 'bluff', 'pilot', 'trice', 'unset', 'dwelt', 'skill', 'corer', 'swamp', 'glint', 'house', 'porch', 'slope', 'rodeo', 'slung', 'stair', 'icing', 'penal', 'flora', 'butte', 'drill', 'dying', 'payer', 'fetus', 'focal', 'blaze', 'dryly', 'abode', 'evoke', 'swung', 'exert', 'shrub', 'aptly', 'relax', 'crony', 'globe', 'craze', 'aorta', 'booze', 'nadir', 'drown', 'these', 'quake', 'berth', 'click', 'jiffy', 'guilt', 'shame', 'botch', 'horse', 'attic', 'morph', 'scamp', 'fence', 'golly', 'cloud', 'image', 'birch', 'aging', 'lunar', 'alive', 'chirp', 'usage', 'flake', 'sharp', 'madam', 'sheik', 'often', 'derby', 'eclat', 'thyme', 'press', 'skate', 'horde', 'vocal', 'comma', 'burst', 'thief', 'broth', 'raise', 'lorry', 'chief', 'frond', 'tract', 'obese', 'shirk', 'dummy', 'bleed', 'stung', 'smite', 'anode', 'piggy', 'milky', 'ardor', 'flare', 'loose', 'mambo', 'repay', 'local', 'easel', 'value', 'oddly', 'mount', 'puppy', 'lover', 'bezel', 'widen', 'stove', 'allay', 'gusty', 'tiara', 'shave', 'doing', 'frost', 'roost', 'cynic', 'elder', 'whirl', 'befit', 'trust', 'molar', 'viola', 'pinch', 'flute', 'roger', 'fifth', 'stoop', 'brand', 'hence', 'covey', 'roach', 'teeth', 'thong', 'spree', 'ethic', 'surer', 'tenet', 'harry', 'rhyme', 'beast', 'alter', 'forty', 'gummy', 'drove', 'shire', 'basis', 'revel', 'poser', 'parse', 'suite', 'creak', 'gauze', 'cower', 'carve', 'glaze', 'piper', 'naive', 'scaly', 'motor', 'panel', 'prawn', 'boxer', 'wound', 'beget', 'strip', 'evade', 'moron', 'armor', 'barge', 'femme', 'fifty', 'leach', 'graft', 'gaffe', 'digit', 'mecca', 'gawky', 'earth', 'terra', 'inlet', 'today', 'gruel', 'umbra', 'found', 'shape', 'exalt', 'jewel', 'ninja', 'skunk', 'curvy', 'pivot', 'madly', 'brake', 'vicar', 'mogul', 'minus', 'chili', 'usual', 'zonal', 'enjoy', 'spark', 'cameo', 'corny', 'minim', 'stain', 'heart', 'thumb', 'taste', 'being', 'bathe', 'lurch', 'spent', 'craft', 'flunk', 'seize', 'tarot', 'saint', 'cider', 'parer', 'modal', 'skulk', 'plead', 'given', 'venom', 'organ', 'camel', 'dozen', 'resin', 'vital', 'savor', 'askew', 'envoy', 'mover', 'chase', 'ruler', 'swore', 'topic', 'bicep', 'ralph', 'medal', 'truck', 'clerk', 'grind', 'input', 'label', 'sooth', 'taunt', 'stank', 'icily', 'algae', 'golem', 'twice', 'spilt', 'grove', 'shove', 'dully', 'heath', 'tripe', 'sauce', 'ombre', 'skier', 'feast', 'hotly', 'spire', 'realm', 'rotor', 'spill', 'flack', 'shown', 'knead', 'tatty', 'sneak', 'ember', 'amber', 'freer', 'bloat', 'awful', 'chain', 'sappy', 'creep', 'mouth', 'treat', 'awash', 'abide', 'short', 'baste', 'geese', 'llama', 'opera', 'slosh', 'wrong', 'flyer', 'drunk', 'smoke', 'large', 'binge', 'alone', 'reach', 'penne', 'nasal', 'folly', 'chess', 'dodge', 'power', 'slice', 'beret', 'pique', 'gauge', 'queen', 'bloke', 'unify', 'badly', 'hazel', 'atone', 'could', 'abyss', 'mourn', 'ashen', 'round', 'lingo', 'apnea', 'swarm', 'brute', 'affix', 'lucid', 'giver', 'daily', 'quack', 'droit', 'gross', 'enemy', 'theme', 'spurt', 'fraud', 'detox', 'pouch', 'drawn', 'floss', 'verve', 'whose', 'sixth', 'winch', 'chose', 'gecko', 'etude', 'depth', 'labor', 'prose', 'erode', 'plain', 'gamer', 'guide', 'jaunt', 'fatal', 'bowel', 'shaft', 'pizza', 'teddy', 'proud', 'pleat', 'where', 'trade', 'panic', 'surge', 'niece', 'haute', 'butch', 'knelt', 'enact', 'axion', 'blunt', 'stalk', 'slept', 'tweed', 'south', 'grace', 'pearl', 'flask', 'blind', 'abuse', 'cramp', 'axiom', 'bully', 'wreck', 'antic', 'unlit', 'nurse', 'downy', 'valid', 'bunch', 'nylon', 'abhor', 'sloth', 'weigh', 'wispy', 'slyly', 'caput', 'swath', 'light', 'bring', 'email', 'fugue', 'weary', 'shyly', 'iliac', 'hippy', 'quirk', 'hunky', 'score', 'ramen', 'adage', 'mimic', 'bingo', 'rouse', 'sober', 'abbot', 'ready', 'bongo', 'rabbi', 'mushy', 'islet', 'expel', 'ascot', 'urine', 'crumb', 'annul', 'phony', 'wrack', 'louse', 'satin', 'stern', 'duvet', 'lower', 'fecal', 'three', 'smoky', 'eight', 'print', 'guile', 'broke', 'stunt', 'jelly', 'hurry', 'sweat', 'leash', 'audit', 'surly', 'glade', 'reuse', 'trend', 'braid', 'khaki', 'fishy', 'wrest', 'broad', 'cress', 'stint', 'wreak', 'forge', 'sally', 'crude', 'toast', 'plant', 'rally', 'quark', 'dimly', 'owner', 'cross', 'about', 'heady', 'inane', 'datum', 'trick', 'petal', 'robin', 'arbor', 'drift', 'crane', 'owing', 'daisy', 'erect', 'heron', 'irate', 'anger', 'teary', 'sigma', 'truss', 'utile', 'bossy', 'actor', 'dense', 'atoll', 'blond', 'cloak', 'savvy', 'sting', 'slick', 'perky', 'sever', 'prank', 'close', 'wring', 'goofy', 'steam', 'bunny', 'spoon', 'hyper', 'avert', 'shall', 'early', 'serve', 'freak', 'valve', 'grate', 'natal', 'gloom', 'stand', 'women', 'mamma', 'worth', 'clamp', 'mangy', 'mirth', 'knoll', 'godly', 'occur', 'breed', 'dough', 'quail', 'plier', 'level', 'apply', 'crump', 'coast', 'pecan', 'pubic', 'cruel', 'youth', 'login', 'judge', 'reply', 'lusty', 'filly', 'waste', 'query', 'wharf', 'bread', 'pixel', 'split', 'cadet', 'aback', 'reset', 'curry', 'impel', 'parka', 'belly', 'bawdy', 'ester', 'dandy', 'usurp', 'gayer', 'meant', 'bloom', 'known', 'chard', 'inter', 'ratty', 'quest', 'await', 'syrup', 'blimp', 'fritz', 'glare', 'cabby', 'navel', 'bland', 'posse', 'utter', 'deity', 'olive', 'funky', 'spade', 'laden', 'stiff', 'tuber', 'state', 'hymen', 'donor', 'elope', 'queer', 'demur', 'tapir', 'knave', 'tonga', 'sepia', 'debit', 'clash', 'unzip', 'bylaw', 'truce', 'curve', 'creek', 'gypsy', 'ultra', 'cutie', 'music', 'snout', 'juice', 'horny', 'whelp', 'shone', 'parry', 'droll', 'recut', 'share', 'gassy', 'ingot', 'speck', 'snipe', 'gully', 'risen', 'midge', 'snail', 'sling', 'lowly', 'scald', 'lemur', 'grain', 'booth', 'logic', 'spray', 'radio', 'dread', 'shore', 'skirt', 'scope', 'turbo', 'snack', 'sheen', 'extra', 'gloss', 'solar', 'chill', 'choir', 'prove', 'macho', 'hyena', 'heist', 'fluid', 'totem', 'agony', 'brood', 'fixer', 'briny', 'fjord', 'vigor', 'guise', 'idiom', 'upper', 'death', 'bound', 'shiny', 'picky', 'medic', 'minty', 'miner', 'wimpy', 'zesty', 'catty', 'paste', 'unmet', 'cheer', 'nasty', 'daunt', 'greet', 'joint', 'speak', 'pesto', 'booby', 'savoy', 'dutch', 'wedge', 'titan', 'whack', 'drink', 'boost', 'trunk', 'foggy', 'ample', 'stunk', 'heavy', 'clone', 'pygmy', 'quote', 'rogue', 'arena', 'nosey', 'awoke', 'crave', 'crept', 'dryer', 'brain', 'field', 'adult', 'offer', 'hitch', 'rowdy', 'tibia', 'buyer', 'incur', 'uncut', 'munch', 'begun', 'scrap', 'abort', 'alloy', 'gravy', 'stamp', 'tamer', 'hover', 'diode', 'tense', 'noose', 'fleck', 'gnome', 'prone', 'canny', 'bison', 'virus', 'vegan', 'salsa', 'flair', 'stare', 'truer', 'helix', 'groan', 'rifle', 'saucy', 'rough', 'hardy', 'slimy', 'chunk', 'segue', 'kappa', 'badge', 'spawn', 'cargo', 'afoot', 'fewer', 'radii', 'grasp', 'harpy', 'guest', 'shied', 'fauna', 'basin', 'trove', 'harem', 'wiser', 'caulk', 'gloat', 'uncle', 'boney', 'tonal', 'aider', 'juror', 'trait', 'verso', 'tweet', 'sissy', 'cliff', 'scout', 'pudgy', 'tithe', 'haven', 'manic', 'trial', 'touch', 'humus', 'tango', 'wagon', 'poker', 'entry', 'furor', 'nymph', 'revue', 'soapy', 'honey', 'soggy']

    all_possibilities = [('grey', 'grey', 'grey', 'grey', 'grey'), ('grey', 'grey', 'grey', 'grey', 'yellow'), ('grey', 'grey', 'grey', 'grey', 'green'), ('grey', 'grey', 'grey', 'yellow', 'yellow'), ('grey', 'grey', 'grey', 'yellow', 'grey'), ('grey', 'grey', 'grey', 'yellow', 'green'), ('grey', 'grey', 'grey', 'green', 'green'), ('grey', 'grey', 'grey', 'green', 'grey'), ('grey', 'grey', 'grey', 'green', 'yellow'), ('grey', 'grey', 'yellow', 'yellow', 'yellow'), ('grey', 'grey', 'yellow', 'yellow', 'grey'), ('grey', 'grey', 'yellow', 'yellow', 'green'), ('grey', 'grey', 'yellow', 'grey', 'grey'), ('grey', 'grey', 'yellow', 'grey', 'green'), ('grey', 'grey', 'yellow', 'grey', 'yellow'), ('grey', 'grey', 'yellow', 'green', 'green'), ('grey', 'grey', 'yellow', 'green', 'grey'), ('grey', 'grey', 'yellow', 'green', 'yellow'), ('grey', 'grey', 'green', 'green', 'green'), ('grey', 'grey', 'green', 'green', 'grey'), ('grey', 'grey', 'green', 'green', 'yellow'), ('grey', 'grey', 'green', 'grey', 'grey'), ('grey', 'grey', 'green', 'grey', 'yellow'), ('grey', 'grey', 'green', 'yellow', 'yellow'), ('grey', 'grey', 'green', 'yellow', 'grey'), ('grey', 'yellow', 'yellow', 'yellow', 'yellow'), ('grey', 'yellow', 'yellow', 'yellow', 'grey'), ('grey', 'yellow', 'yellow', 'yellow', 'green'), ('grey', 'yellow', 'yellow', 'grey', 'grey'), ('grey', 'yellow', 'yellow', 'grey', 'green'), ('grey', 'yellow', 'yellow', 'grey', 'yellow'), ('grey', 'yellow', 'yellow', 'green', 'green'), ('grey', 'yellow', 'yellow', 'green', 'grey'), ('grey', 'yellow', 'yellow', 'green', 'yellow'), ('grey', 'yellow', 'grey', 'grey', 'grey'), ('grey', 'yellow', 'grey', 'grey', 'green'), ('grey', 'yellow', 'grey', 'grey', 'yellow'), ('grey', 'yellow', 'grey', 'green', 'green'), ('grey', 'yellow', 'grey', 'green', 'grey'), ('grey', 'yellow', 'grey', 'green', 'yellow'), ('grey', 'yellow', 'grey', 'yellow', 'yellow'), ('grey', 'yellow', 'grey', 'yellow', 'grey'), ('grey', 'yellow', 'green', 'green', 'green'), ('grey', 'yellow', 'green', 'green', 'grey'), ('grey', 'yellow', 'green', 'green', 'yellow'), ('grey', 'yellow', 'green', 'grey', 'grey'), ('grey', 'yellow', 'green', 'grey', 'yellow'), ('grey', 'yellow', 'green', 'yellow', 'yellow'), ('grey', 'yellow', 'green', 'yellow', 'grey'), ('grey', 'green', 'green', 'green', 'green'), ('grey', 'green', 'green', 'green', 'grey'), ('grey', 'green', 'green', 'green', 'yellow'), ('grey', 'green', 'green', 'grey', 'grey'), ('grey', 'green', 'green', 'grey', 'yellow'), ('grey', 'green', 'green', 'yellow', 'yellow'), ('grey', 'green', 'green', 'yellow', 'grey'), ('grey', 'green', 'grey', 'grey', 'grey'), ('grey', 'green', 'grey', 'grey', 'yellow'), ('grey', 'green', 'grey', 'yellow', 'yellow'), ('grey', 'green', 'grey', 'yellow', 'grey'), ('grey', 'green', 'yellow', 'yellow', 'yellow'), ('grey', 'green', 'yellow', 'yellow', 'grey'), ('grey', 'green', 'yellow', 'grey', 'grey'), ('yellow', 'yellow', 'yellow', 'yellow', 'yellow'), ('yellow', 'yellow', 'yellow', 'yellow', 'grey'), ('yellow', 'yellow', 'yellow', 'yellow', 'green'), ('yellow', 'yellow', 'yellow', 'grey', 'grey'), ('yellow', 'yellow', 'yellow', 'grey', 'green'), ('yellow', 'yellow', 'yellow', 'grey', 'yellow'), ('yellow', 'yellow', 'yellow', 'green', 'green'), ('yellow', 'yellow', 'yellow', 'green', 'grey'), ('yellow', 'yellow', 'yellow', 'green', 'yellow'), ('yellow', 'yellow', 'grey', 'grey', 'grey'), ('yellow', 'yellow', 'grey', 'grey', 'green'), ('yellow', 'yellow', 'grey', 'grey', 'yellow'), ('yellow', 'yellow', 'grey', 'green', 'green'), ('yellow', 'yellow', 'grey', 'green', 'grey'), ('yellow', 'yellow', 'grey', 'green', 'yellow'), ('yellow', 'yellow', 'grey', 'yellow', 'yellow'), ('yellow', 'yellow', 'grey', 'yellow', 'grey'), ('yellow', 'yellow', 'green', 'green', 'green'), ('yellow', 'yellow', 'green', 'green', 'grey'), ('yellow', 'yellow', 'green', 'green', 'yellow'), ('yellow', 'yellow', 'green', 'grey', 'grey'), ('yellow', 'yellow', 'green', 'grey', 'yellow'), ('yellow', 'yellow', 'green', 'yellow', 'yellow'), ('yellow', 'yellow', 'green', 'yellow', 'grey'), ('yellow', 'grey', 'grey', 'grey', 'grey'), ('yellow', 'grey', 'grey', 'grey', 'green'), ('yellow', 'grey', 'grey', 'grey', 'yellow'), ('yellow', 'grey', 'grey', 'green', 'green'), ('yellow', 'grey', 'grey', 'green', 'grey'), ('yellow', 'grey', 'grey', 'green', 'yellow'), ('yellow', 'grey', 'grey', 'yellow', 'yellow'), ('yellow', 'grey', 'grey', 'yellow', 'grey'), ('yellow', 'grey', 'green', 'green', 'green'), ('yellow', 'grey', 'green', 'green', 'grey'), ('yellow', 'grey', 'green', 'green', 'yellow'), ('yellow', 'grey', 'green', 'grey', 'grey'), ('yellow', 'grey', 'green', 'grey', 'yellow'), ('yellow', 'grey', 'green', 'yellow', 'yellow'), ('yellow', 'grey', 'green', 'yellow', 'grey'), ('yellow', 'grey', 'yellow', 'yellow', 'yellow'), ('yellow', 'grey', 'yellow', 'yellow', 'grey'), ('yellow', 'grey', 'yellow', 'grey', 'grey'), ('yellow', 'green', 'green', 'green', 'green'), ('yellow', 'green', 'green', 'green', 'grey'), ('yellow', 'green', 'green', 'green', 'yellow'), ('yellow', 'green', 'green', 'grey', 'grey'), ('yellow', 'green', 'green', 'grey', 'yellow'), ('yellow', 'green', 'green', 'yellow', 'yellow'), ('yellow', 'green', 'green', 'yellow', 'grey'), ('yellow', 'green', 'grey', 'grey', 'grey'), ('yellow', 'green', 'grey', 'grey', 'yellow'), ('yellow', 'green', 'grey', 'yellow', 'yellow'), ('yellow', 'green', 'grey', 'yellow', 'grey'), ('yellow', 'green', 'yellow', 'yellow', 'yellow'), ('yellow', 'green', 'yellow', 'yellow', 'grey'), ('yellow', 'green', 'yellow', 'grey', 'grey'), ('green', 'green', 'green', 'green', 'green'), ('green', 'green', 'green', 'green', 'grey'), ('green', 'green', 'green', 'green', 'yellow'), ('green', 'green', 'green', 'grey', 'grey'), ('green', 'green', 'green', 'grey', 'yellow'), ('green', 'green', 'green', 'yellow', 'yellow'), ('green', 'green', 'green', 'yellow', 'grey'), ('green', 'green', 'grey', 'grey', 'grey'), ('green', 'green', 'grey', 'grey', 'yellow'), ('green', 'green', 'grey', 'yellow', 'yellow'), ('green', 'green', 'grey', 'yellow', 'grey'), ('green', 'green', 'yellow', 'yellow', 'yellow'), ('green', 'green', 'yellow', 'yellow', 'grey'), ('green', 'green', 'yellow', 'grey', 'grey'), ('green', 'grey', 'grey', 'grey', 'grey'), ('green', 'grey', 'grey', 'grey', 'yellow'), ('green', 'grey', 'grey', 'yellow', 'yellow'), ('green', 'grey', 'grey', 'yellow', 'grey'), ('green', 'grey', 'yellow', 'yellow', 'yellow'), ('green', 'grey', 'yellow', 'yellow', 'grey'), ('green', 'grey', 'yellow', 'grey', 'grey'), ('green', 'yellow', 'yellow', 'yellow', 'yellow'), ('green', 'yellow', 'yellow', 'yellow', 'grey'), ('green', 'yellow', 'yellow', 'grey', 'grey'), ('green', 'yellow', 'grey', 'grey', 'grey')]



letters = ["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]
yellow_letters = list()


def possible_words(letters, yellow_letters):
    possibilities = list()
    for word in words:
        print_term = True
        for pos in range(5):
            if word[pos : pos + 1] not in letters[pos]:
                print_term = False
                break
        if not print_term:
            continue
        for letter in yellow_letters:
            if letter not in word or yellow_letters.count(letter) != word.count(letter):
                print_term = False
                break
        if print_term:
            possibilities.append(word)
    return possibilities


def modify_letters():
    global letters
    for letter in range(len(word)):
        char = word[letter : letter + 1]
        if letter_categories[letter] == "grey":
            if char not in yellow_letters:
                for letter_z in range(len(letters)):
                    if char != letters[letter_z]:
                        pos = letters[letter_z].find(char)
                        if pos > -1:
                            letters[letter_z] = letters[letter_z][:pos] + letters[letter_z][pos + 1:]
        elif letter_categories[letter] == "green":
            letters[letter] = char
        elif letter_categories[letter] == "yellow":
            pos = letters[letter].find(char)
            letters[letter] = letters[letter][:pos] + letters[letter][pos + 1:]
            yellow_letters.append(char)


def get_possibilities(word):
    available_possibilities = list()
    for possibility in all_possibilities:
        yellow_letters = dict()
        for element in range(len(possibility)):
            if possibility[element] == "yellow":
                yellow_letters[word[element : element + 1]] = True
        for element in range(len(possibility)):
            if possibility[element] == "yellow" and word.find(word[element : element + 1]) == element and yellow_letters[word[element : element + 1]]:
                yellow_letters[word[element : element + 1]] = False
        if list(yellow_letters.values()).count(True) == 0 or len(list(yellow_letters)) == 0:
            available_possibilities.append(possibility)
    return available_possibilities

counter = 1
with open('wordle_information.json', 'r') as openfile:
    # Reading from json file
    information_dict = json.load(openfile)

for word in words:
    if word not in list(information_dict.keys()):
        total_information = 0
        information_array = {"possibility": list(), "probability": list(), "information": list(), "weighted_information": list()}
        for possibility in get_possibilities(word):
            letter_categories = list(possibility)
            letters = ["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]
            yellow_letters = list()
            modify_letters()
            all_possible_words = possible_words(letters, yellow_letters)
            probability = len(possible_words(letters, yellow_letters)) / len(words)
            if probability == 0:
                continue
            information = math.log(1 / probability, 2)
            weighted_information = probability * information
            total_information += weighted_information


        print(str(counter) + ".", word, "=", total_information)
        information_dict[word] = total_information

        counter += 1

import numpy as np

# Serializing json
json_object = json.dumps(information_dict, indent=4)
with open("wordle_information.json", "w") as outfile:
    outfile.write(json_object)
    # counter += 1
# {k: v for k, v in sorted(information_dict.items(), key=lambda item: item[1])}
print(list(sorted(information_dict.items(), key=lambda item: item[1])))
