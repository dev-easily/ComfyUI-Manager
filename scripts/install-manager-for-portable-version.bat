.\python_embeded\python.exe -s -m pip install gitpython
.\python_embeded\python.exe -c "import git; git.Repo.clone_from('https://github.com/dev-easily/ComfyUI-Manager', './ComfyUI/custom_nodes/ComfyUI-Manager')"
.\python_embeded\python.exe -m pip install -r ./ComfyUI/custom_nodes/ComfyUI-Manager/requirements.txt
