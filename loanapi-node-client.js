const http = require('http')

url = 'http://45.82.72.48:8080/loan-api/v1'
//url = 'http://0.0.0.0:8080/loan-api/v1'

http.get(url+'/loans/1',res=>{
    console.log(`statusCode: ${res.statusCode}`)

    res.on('data', d => {
        console.log(d)
    })
  
  req.on('error', error => {
    console.error(error)
  })
  
  req.end()
})