// var elems = {
// 	tl: [ document.getElementById('btn-tl'), document.getElementById('tl') ],
// 	tr: [ document.getElementById('btn-tr'), document.getElementById('tr') ],
// 	bl: [ document.getElementById('btn-bl'), document.getElementById('bl') ],
// 	br: [ document.getElementById('btn-br'), document.getElementById('br') ],
// 	tick: [ document.getElementById('btn-tick'), document.getElementById('tick') ],
// 	cross: [ document.getElementById('btn-cross'), document.getElementById('cross') ]
// };

// document.getElementById('btn-cl').addEventListener('click', rmvall)

// Object.values(elems).map((elem) => {
// 	elem[0].addEventListener('click', () => {
// 		Object.values(elems).map((elem) => {
// 			elem[1].classList.remove('visible');
// 		});
// 		elem[1].classList.add('visible');
// 	});
// });

// function rmvall() {
// 	Object.values(elems).map((elem) => {
// 		elem[1].classList.remove('visible');
// 	});
// };

const remove = () => {
	document.querySelectorAll('.arrow').forEach((e) => { e.classList.remove('visible'); });
};

const makeVisible = (selector) => {
	remove();
	document.getElementById(selector).classList.add('visible');
};

let highScore = 0;

const updateScore = (score) => {
    document.getElementById('score').innerHTML = score;
    if(score > highScore) {
        highScore = score
        document.getElementById('highScore').innerHTML = highScore;
    }
};

const getMove = () => {
	$.ajax({url: '/result', timeout: 80, success: (data) => {
        if(data.length > 2 && data !== 'clear') {
            data = data.split(' ');
            let score = data.length > 1 ? data[1].slice('1') : 0;
            updateScore(score);
            data = data[0];
        }
		switch(data) {
			case 'tr':
				makeVisible('tr');
				break;
			case 'tl':
				makeVisible('tl')
				break;
			case 'br':
				makeVisible('br')
				break;
			case 'bl':
				makeVisible('bl')
				break;
			case 'tick':
				makeVisible('tick')
				break;
			case 'cross':
				makeVisible('cross')
				break;
			case 'clear':
				remove();
				break;
		}
	}});
};

(() => {
	setInterval(getMove, 100);
})();