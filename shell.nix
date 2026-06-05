{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  buildInputs = [
    (pkgs.python312.withPackages (
      ps: with ps; [
        pip
        pandas
        numpy
        scipy
        openpyxl
        matplotlib
        dlib
        face-recognition
      ]
    ))
  ];
}
