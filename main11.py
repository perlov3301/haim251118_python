# using cmd for running function
import typer
app = typer.Typer()
@app.command()
def hello(name:str, num:int) -> None:
    i=num
    while i>0:
      print(f"Hello {name}")
      i-=1
@app.command()
def goodbye(name:str, num:int) -> None:
    i=num
    while i>0:
     print(f"Goodbye {name}")
     i-=1
if __name__ == "__main__":
    app()