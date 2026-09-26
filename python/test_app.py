import runpy

from app import main

def test_main_output(capsys):
    main()

    captured = capsys.readouterr()

    esperado = "Python funcionando" + chr(10) +"Python configurado" + chr(10)

    assert captured.out == esperado

def test_execucao_como_programa(capsys):
    runpy.run_path("app.py",run_name="__main__")

    captured = capsys.readouterr()

    esperado = "Python funcionando" + chr(10) + "Python configurado" + chr(10)

    assert captured.out == esperado
