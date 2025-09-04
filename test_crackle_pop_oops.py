#!/usr/bin/env python3

import sys
import crackle_pop

def test_main_divisible_by_5(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["crackle_pop.py"])
    crackle_pop.main()
    captured = capsys.readouterr()
    assert "Please" in captured.out
    
