import numpy as np
import unittest
import discretize


class TestInnerProductsDerivsTensor(unittest.TestCase):
    def doTestFace(
        self, h, rep, fast, meshType, invert_model=False, invert_matrix=False
    ):
        if meshType == "Curv":
            hRect = discretize.utils.example_curvilinear_grid(h, "rotate")
            mesh = discretize.CurvilinearMesh(hRect)
        elif meshType == "Tree":
            mesh = discretize.TreeMesh(h, levels=3)
            mesh.refine(lambda xc: 3)
        elif meshType == "Tensor":
            mesh = discretize.TensorMesh(h)
        v = np.random.rand(mesh.nF)
        sig = np.random.rand(1) if rep == 0 else np.random.rand(mesh.nC * rep)

        def fun(sig):
            M = mesh.get_face_inner_product(
                sig, invert_model=invert_model, invert_matrix=invert_matrix
            )
            Md = mesh.get_face_inner_product_deriv(
                sig,
                invert_model=invert_model,
                invert_matrix=invert_matrix,
                do_fast=fast,
            )
            return M * v, Md(v)

        print(
            meshType,
            "Face",
            h,
            rep,
            fast,
            ("harmonic" if invert_model and invert_matrix else "standard"),
        )
        return discretize.tests.check_derivative(fun, sig, num=5, plotIt=False)

    def doTestEdge(
        self, h, rep, fast, meshType, invert_model=False, invert_matrix=False
    ):
        if meshType == "Curv":
            hRect = discretize.utils.example_curvilinear_grid(h, "rotate")
            mesh = discretize.CurvilinearMesh(hRect)
        elif meshType == "Tree":
            mesh = discretize.TreeMesh(h, levels=3)
            mesh.refine(lambda xc: 3)
        elif meshType == "Tensor":
            mesh = discretize.TensorMesh(h)
        v = np.random.rand(mesh.nE)
        sig = np.random.rand(1) if rep == 0 else np.random.rand(mesh.nC * rep)

        def fun(sig):
            M = mesh.get_edge_inner_product(
                sig, invert_model=invert_model, invert_matrix=invert_matrix
            )
            Md = mesh.get_edge_inner_product_deriv(
                sig,
                invert_model=invert_model,
                invert_matrix=invert_matrix,
                do_fast=fast,
            )
            return M * v, Md(v)

        print(
            meshType,
            "Edge",
            h,
            rep,
            fast,
            ("harmonic" if invert_model and invert_matrix else "standard"),
        )
        return discretize.tests.check_derivative(fun, sig, num=5, plotIt=False)

    def test_FaceIP_2D_float_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 0, False, "Tree"))

    def test_FaceIP_3D_float_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 0, False, "Tree"))

    def test_FaceIP_2D_isotropic_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 1, False, "Tree"))

    def test_FaceIP_3D_isotropic_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 1, False, "Tree"))

    def test_FaceIP_2D_anisotropic_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 2, False, "Tree"))

    def test_FaceIP_3D_anisotropic_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 3, False, "Tree"))

    def test_FaceIP_2D_tensor_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 3, False, "Tree"))

    def test_FaceIP_3D_tensor_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 6, False, "Tree"))

    def test_FaceIP_2D_float_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 0, True, "Tree"))

    def test_FaceIP_3D_float_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 0, True, "Tree"))

    def test_FaceIP_2D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 1, True, "Tree"))

    def test_FaceIP_3D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 1, True, "Tree"))

    def test_FaceIP_2D_anisotropic_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 2, True, "Tree"))

    def test_FaceIP_3D_anisotropic_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 3, True, "Tree"))

    # def test_EdgeIP_2D_float_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 0, False, 'Tree'))
    def test_EdgeIP_3D_float_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 0, False, "Tree"))

    # def test_EdgeIP_2D_isotropic_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 1, False, 'Tree'))

    def test_EdgeIP_3D_isotropic_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 1, False, "Tree"))

    # def test_EdgeIP_2D_anisotropic_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 2, False, 'Tree'))

    def test_EdgeIP_3D_anisotropic_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 3, False, "Tree"))

    # def test_EdgeIP_2D_tensor_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 3, False, 'Tree'))

    def test_EdgeIP_3D_tensor_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 6, False, "Tree"))

    # def test_EdgeIP_2D_float_fast_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 0, True, 'Tree'))
    def test_EdgeIP_3D_float_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 0, True, "Tree"))

    # def test_EdgeIP_2D_isotropic_fast_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 1, True, 'Tree'))

    def test_EdgeIP_3D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 1, True, "Tree"))

    # def test_EdgeIP_2D_anisotropic_fast_Tree(self):
    #     self.assertTrue(self.doTestEdge([8, 8], 2, True, 'Tree'))

    def test_EdgeIP_3D_anisotropic_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 3, True, "Tree"))


class TestFacePropertiesInnerProductsDerivsTensor(unittest.TestCase):
    def doTestFace(self, h, rep, meshType, invert_model=False, invert_matrix=False):
        if meshType == "Curv":
            hRect = discretize.utils.example_curvilinear_grid(h, "rotate")
            mesh = discretize.CurvilinearMesh(hRect)
        elif meshType == "Tree":
            mesh = discretize.TreeMesh(h, levels=3)
            mesh.refine(lambda xc: 3)
        elif meshType == "Tensor":
            mesh = discretize.TensorMesh(h)
        v = np.random.rand(mesh.nF)
        sig = np.random.rand(1) if rep == 0 else np.random.rand(mesh.nF * rep)

        def fun(sig):
            M = mesh.get_face_inner_product_surface(
                sig, invert_model=invert_model, invert_matrix=invert_matrix
            )
            Md = mesh.get_face_inner_product_surface_deriv(
                sig,
                invert_model=invert_model,
                invert_matrix=invert_matrix,  # , do_fast=fast
            )
            return M * v, Md(v)

        print(
            meshType,
            "Face",
            h,
            rep,
            # fast,
            ("harmonic" if invert_model and invert_matrix else "standard"),
        )
        return discretize.tests.check_derivative(fun, sig, num=5, plotIt=False)

    def doTestEdge(self, h, rep, meshType, invert_model=False, invert_matrix=False):
        if meshType == "Curv":
            hRect = discretize.utils.example_curvilinear_grid(h, "rotate")
            mesh = discretize.CurvilinearMesh(hRect)
        elif meshType == "Tree":
            mesh = discretize.TreeMesh(h, levels=3)
            mesh.refine(lambda xc: 3)
        elif meshType == "Tensor":
            mesh = discretize.TensorMesh(h)
        v = np.random.rand(mesh.nE)
        sig = np.random.rand(1) if rep == 0 else np.random.rand(mesh.nF * rep)

        def fun(sig):
            M = mesh.get_edge_inner_product_surface(
                sig, invert_model=invert_model, invert_matrix=invert_matrix
            )
            Md = mesh.get_edge_inner_product_surface_deriv(
                sig,
                invert_model=invert_model,
                invert_matrix=invert_matrix,  # , do_fast=fast
            )
            return M * v, Md(v)

        print(
            meshType,
            "Edge",
            h,
            rep,
            # fast,
            ("harmonic" if invert_model and invert_matrix else "standard"),
        )
        return discretize.tests.check_derivative(fun, sig, num=5, plotIt=False)

    def test_FaceIP_2D_float_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 0, "Tree"))

    def test_FaceIP_3D_float_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 0, "Tree"))

    def test_FaceIP_2D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8], 1, "Tree"))

    def test_FaceIP_3D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestFace([8, 8, 8], 1, "Tree"))

    def test_EdgeIP_2D_float_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8], 0, "Tree"))

    def test_EdgeIP_3D_float_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 0, "Tree"))

    def test_EdgeIP_2D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8], 1, "Tree"))

    def test_EdgeIP_3D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 1, "Tree"))


class TestEdgePropertiesInnerProductsDerivsTensor(unittest.TestCase):
    def doTestEdge(self, h, rep, meshType, invert_model=False, invert_matrix=False):
        if meshType == "Curv":
            hRect = discretize.utils.example_curvilinear_grid(h, "rotate")
            mesh = discretize.CurvilinearMesh(hRect)
        elif meshType == "Tree":
            mesh = discretize.TreeMesh(h, levels=3)
            mesh.refine(lambda xc: 3)
        elif meshType == "Tensor":
            mesh = discretize.TensorMesh(h)
        v = np.random.rand(mesh.nE)
        sig = np.random.rand(1) if rep == 0 else np.random.rand(mesh.nE * rep)

        def fun(sig):
            M = mesh.get_edge_inner_product_line(
                sig, invert_model=invert_model, invert_matrix=invert_matrix
            )
            Md = mesh.get_edge_inner_product_line_deriv(
                sig,
                invert_model=invert_model,
                invert_matrix=invert_matrix,  # , do_fast=fast
            )
            return M * v, Md(v)

        print(
            meshType,
            "Edge",
            h,
            rep,
            # fast,
            ("harmonic" if invert_model and invert_matrix else "standard"),
        )
        return discretize.tests.check_derivative(fun, sig, num=5, plotIt=False)

    def test_EdgeIP_2D_float_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8], 0, "Tree"))

    def test_EdgeIP_3D_float_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 0, "Tree"))

    def test_EdgeIP_2D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8], 1, "Tree"))

    def test_EdgeIP_3D_isotropic_fast_Tree(self):
        self.assertTrue(self.doTestEdge([8, 8, 8], 1, "Tree"))
