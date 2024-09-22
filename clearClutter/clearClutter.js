const fs= require("fs/promises")
const fsn= require("fs")
const path= require("path");

const myPath="C:\\Users\\Lenovo\\Desktop\\VS Files\\Sigma Web Development Course\\clearClutter"

let files;
let ext;
async function readDir(){
    files=await fs.readdir(myPath)
    for (const file of files) {
        ext=path.extname(file)
        ext=ext.split(".")[1] //split function return objext , so have to give index
        if (ext!="js" && file.split(".").length>1) {
            if (fsn.existsSync(path.join(myPath , ext))) {
                //if path exist then it will replace the existing path to mypath> ext filder > then files , Hence files will b earranged and clutter wull be cleared
                fs.rename(path.join(myPath , file) , path.join(myPath , ext , file)) //rename replace the first path with second
            } else {
                fs.mkdir(ext)
                fs.rename(path.join(myPath , file) , path.join(myPath , ext , file))
            }
        }
    }
}
readDir()


