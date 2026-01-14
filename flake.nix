{
  description = "Jekyll development environment for CSCI 432";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            ruby
            bundler
            git
          ];

          shellHook = ''
            export GEM_HOME=$PWD/.gem
            export PATH=$GEM_HOME/bin:$PATH

            echo "Jekyll development environment loaded!"
            echo ""
            echo "To get started:"
            echo "  1. Run 'bundle install' to install dependencies"
            echo "  2. Run 'bundle exec jekyll serve' to start the server"
            echo ""
          '';
        };
      }
    );
}
