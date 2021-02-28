document.addEventListener('DOMContentLoaded', () => 
{
  const startBtn = document.querySelector('button')
  const grid = document.querySelector('.grid')
  const scoreDisplay = document.querySelector('.score-display')
  const lineDisplay = document.querySelector('.lines-display')
  const displaySquares = document.querySelectorAll('.previous-grid div')
  let squares = Array.from(grid.querySelectorAll('div'))
  let currentIndex = 0
  const width = 10
  const height = 20
  let currentPosition = 4
  let timerID
  
  //assign keys
  function control(e)
  {
    if(e.KeyCode === 39)
    {
      moveRight()
    }
    else if (e.KeyCode === 38)
    {
      rotate()
    }
    else if (e.KeyCode ===37)
    {
      moveLeft()
    }
    else if (e.KeyCode === 40)
    {
      moveDown()
    }
  }
  document.addEventListener('keyup', control)

  //The Tetrominoes
  const lTetromino = [
    [1, width+1, width*2+1, 2],
    [width, width+1, width+2, width*2+2],
    [1, width+1, width*2+1, width*2],
    [width, width*2, width*2+1, width*2+2]
  ]

  const zTetromino = [
    [0, width, width+1, width*2+1],
    [width+1, width+2, width*2, width*2+1],
    [0, width, width+1, width*2+1],
    [width+1, width+2, width*2, width*2+1]
  ]

  const tTetromino = [
    [1, width, width+1, width+2],
    [1, width+1, width+2, width*2+1],
    [width, width*2, width*2+1, width*2+1],
    [1, width, width+1, width*2+1]
  ]

  const oTetromino = [
    [0, 1, width, width+1],
    [0, 1, width, width+1],
    [0, 1, width, width+1],
    [0, 1, width, width+1]
  ]

  const iTetromino = [
    [1, width+1, width*2+1, width*3+1],
    [width, width+1, width+2, width+3],
    [1, width+1, width*2+1, width*3+1],
    [width, width+1, width+2, width+3]
  ]

  const theTetrominoes = [lTetromino, zTetromino, tTetromino, oTetromino, iTetromino]

  //random
  let random = Math.floor(Math.random()*theTetrominoes.length)
  let currentRotation = 0
  let current = theTetrominoes[random][currentRotation]


  //draw
  function draw()
  {
    current.forEach( index => (
      squares[currentPosition + index].classList.add('block')
    ))
  }
  //undraw
  function undraw()
  {
    current.forEach( index => (
      squares[currentPosition + index].classList.remove('block')
    ))
  }
    
  //move down
  function moveDown(){
    undraw()
    currentPosition = currentPosition +=width
    draw()
    freeze()
  }

  function moveRight()
  {
    undraw()
    const isAtRightEdge = current.some(index => (currentPosition + index) % width === width - 1)
    if(!isAtRightEdge) currentPosition +=1
    if (current.some(index => squares[currentPosition + index].classList.contains('block2')))
    {
      currentPosition-=1
    }
    draw()
  }

  function moveLeft()
  {
    undraw()
    const isAtRightEdge = current.some(index => (currentPosition + index) % width === 0)
    if(!isAtRightEdge) currentPosition -=1
    if (current.some(index => squares[currentPosition + index].classList.contains('block2')))
    {
      currentPosition+=1
    }
    draw()
  }

  //rotate
  function rotate()
  {
    undraw()
    currentRotation++
    if(currentRotation === current.length)
    {
      currentRotation = 0
    }
    current = theTetrominoes[random][currentRotation]
    draw()
  } 
}) 
//show previous

const displayWidth = 4
const displayIndex = 0
let nextRandom = 0

const smallTetrominoes = [
  [1, displayWidth+1, displayWidth*2+1, 2],
  [0, displayWidth, displayWidth+1, displayWidth*2+1],
  [1, displayWidth, displayWidth+1, displayWdth+2],
  [0, 1, displayWidth, displayWidth+1],
  [1, displayWidth+1, displayWidth*2+1, displayWidth*3+1]
]

function displayShape()
{
  displaySquarers.forEach(squares => {
    squares.classList.remove('block')
  })
  smallTetrominoes[nextRandom].forEach( index => {
    displaySquares[displayIndex + index].classList.add('block')
  })
}

function freeze()
{
  if(current.some(index => squares[currentPosition + index + width].classList.contains('block3') 
  || squares[currentPosition + index + width].classList.contains('block2')))
  {
    current.forEach(index => squares[index + currentPosition].classList.add('block2'))

    random = nextRandom
    nextRandom = Math.floor(Math.random() * theTetrominoes.length)
    curret = theTetrominoes[random][currentPosition]
    currentPosition = 4
    draw()
    displayShape()
  }
}

startBtn.addEventListener('click', () => {
  if (timerID) {
    clearInterval(timerID)
    timerID = null
  }
  else
  {
    draw()
    timerID = setInterval(moveDown, 1000)
    nextRandom = Math.floor(Math.random()*theTetrominoes.length)
    displayShape()
  }
})

//game over
function gameOver()
{
  if(current.some(indexe => squares[currentPosition + index].classList.contains('block2')))
  {
    scoreDisplay.innerHTML = 'end'
    clearInterval(timerID)
  }
}

//add score

function addScore()
{
  for (currentIndex = 0; currentIndex < 199; currentIndex +=width)
  {
    const row = [currentIndex, currentIndex+1, currentIndex+2, currentIndex+3, currentIndex+4,
      currentIndex+5, currentIndex+6, currentIndex+7, currentIndex+8, currentIndex+9, currentIndex]

      if(row.every(index => squares[index].classList.contains('block2')))
      {
        score +=20
        lines+=1
        scoreDisplay.innerHTML = score
        lineDisplay.innerHTML = lines
        row.forEach(index => {
          squares[index].classList.remove('block2') || squares[index].classList.remove('blcok')
        })
        //splice array
        const squaresRemoved = squares.splice(currentIndex, width)
        squares = squaresRemoved.concat(squares)
        squares.forEach(cell => grid.appendChild(cell))
      }
  }
}