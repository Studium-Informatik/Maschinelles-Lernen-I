{
  description = "Environment for Jupyter Notebooks";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";

  outputs = { nixpkgs, ... }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
    in
    {
      devShells = nixpkgs.lib.genAttrs systems (system:
        let
          pkgs = import nixpkgs { inherit system; };
          python = pkgs.python313.withPackages (ps: [
            ps.ipykernel
            ps.jupyterlab
            ps.matplotlib
            ps.numpy
            ps.pillow
            ps.scikit-learn
          ]);
          # Use this environment even if a user-level python3 kernel exists.
          kernel = pkgs.writeTextDir "share/jupyter/kernels/python3/kernel.json"
            (builtins.toJSON {
              argv = [ "${python}/bin/python" "-m" "ipykernel_launcher" "-f" "{connection_file}" ];
              display_name = "Python 3 (sheet03)";
              language = "python";
            });
        in
        {
          default = pkgs.mkShell {
            packages = [ python ];
            JUPYTER_PATH = "${kernel}/share/jupyter";
            PYTHONNOUSERSITE = "1";
          };
        });
    };
}
