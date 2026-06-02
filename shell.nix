{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  buildInputs = [
    (pkgs.python314.withPackages (
      ps: with ps; [
        pip
        pandas
        numpy
        scipy
        openpyxl
        matplotlib
      ]
    ))
  ];
}
